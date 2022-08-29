from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

# 1 option inline keyboard
choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='Buy a pear',
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text='Buy an apples',
                                          callback_data=buy_callback.new(item_name='apple',
                                                                         quantity=5)
                                          # callback_data = 'buy:apple:5'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Cancel',
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

# 2 option inline keyboard
pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = 'https://lenta.com/product/grusha-konferenc-ves-1kg-044185/'

pear_link = InlineKeyboardButton(
    text='Buy here',
    url=PEAR_LINK
)

pear_keyboard.insert(pear_link)

apple_keyboard = InlineKeyboardMarkup()

APPLE_LINK = 'https://lenta.com/product/yabloki-royal-gala-ves-1kg-368105/'

apple_link = InlineKeyboardButton(
    text='Buy here',
    url=APPLE_LINK
)

apple_keyboard.insert(apple_link)
