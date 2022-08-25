from re import compile

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp


# This handler is used for deeplink in private messages
# When the user follows the link http://t.me/username_bot?start=123
# Then, by pressing the /start, the bot receives the /start with the argument 123
# We can catch this deeplink using regular expressions (compile function)
# /d/d/d means that we catch 3 digits in a row. (/d is one digit)
@dp.message_handler(CommandStart(deep_link=compile(r'\d\d\d')), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    # Using the get_args() function, we get the arguments after /start (for the example above it will be '123')
    deep_link_args = message.get_args()
    await message.answer(f'Hello, {message.from_user.full_name}!\n'
                         f'You are in private correspondence.\n'
                         f'There is a deep link in your request\n'
                         f'You passed an argument {deep_link_args}.\n')


# In this handler, we catch a simple click on / start, which did not pass under the condition above
@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
async def bot_start(message: types.Message):
    # To create a deeplink link, you need to get the username of the bot
    # First option
    # bot_user = await dp.bot.get_me()
    # deep_link = f'http://t.me/{bot_user.username}?start=123'
    # Second option
    deep_link = await get_start_link('123')
    await message.answer(f'Hello, {message.from_user.full_name}!\n'
                         f'You are in private correspondence.\n'
                         f'There isn not a deep link in your request\n'
                         f'your deeplink link - {deep_link}\n'
                         f'Your telegram id - {message.from_user.id}')
