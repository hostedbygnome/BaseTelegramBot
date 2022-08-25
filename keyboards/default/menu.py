from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Burgers')
        ],
        [
            KeyboardButton(text='Spaghetti'),
            KeyboardButton(text='Pizza')
        ]
    ],
    resize_keyboard=True
)