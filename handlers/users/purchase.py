import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apple_keyboard
from loader import dp, bot


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='We have 2 items for sale: 5 apples and 1 pear.\n'
                              'If you do not need anything, press the cancel button',
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    # With callback query id
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You chose to buy pears. Whole pears: {quantity}. thank you',
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(text_contains='pear')
async def buying_apple(call: CallbackQuery, callback_data: dict):
    # With callback query id
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You chose to buy apples. Whole apples: {quantity}. thank you',
                              reply_markup=apple_keyboard)


@dp.callback_query_handler(text='Cancel')
async def cancel_buying(call: CallbackQuery):
    # Window with alert
    await call.answer('You have canceled this purchase!',
                      show_alert=True)

    # 1 option send a blank keyboard while modifying messages to remove it from the message
    await call.message.edit_reply_markup(reply_markup=None)

    # 2 option keyboard sends (by API)
    await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=None)
