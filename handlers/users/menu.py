from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Choose a product from the menu below', reply_markup=menu)


@dp.message_handler(text='Burgers')
async def get_burgers(message: types.Message):
    await message.answer('You chosen burgers')


@dp.message_handler(Text(equals=['Spaghetti', 'Pizza']))
async def get_food(message: types.Message):
    await message.answer(f'You chosen {message.text}', reply_markup=ReplyKeyboardRemove())
