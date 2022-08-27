from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold, hcode, hitalic, hstrikethrough, hlink

from loader import dp

html_text = '\n'.join(
    [
        'Hello, ' + hbold('user'),
        hitalic('You need to be afraid not of death, but of an empty life'),
        hstrikethrough('You need to be careful'),
        'This text is html formatted'
        'You can read about it ' + hlink('here', 'https://core.telegram.org/bots/api#formatting-options')
    ]
)

html_text += hcode(html_text)


@dp.message_handler(Command('parse_mode'))
async def show_parse_mode(message: types.Message):
    await message.answer(html_text, parse_mode=types.ParseMode.HTML)
