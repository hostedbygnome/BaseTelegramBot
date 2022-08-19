from aiogram import types
from loader import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    # Get chat_id and text from message
    chat_id = message.from_user.id
    text = message.text

    # Get bot object - from dispatcher
    # bot = dp.bot

    # Get bot object - from context
    # from aiogram import Bot
    # bot = Bot.get_current()

    # Get bot object - from loader module
    from  loader import bot

    # Send message to user - 1 option
    await bot.send_message(chat_id=chat_id, text=text)

    # Send message to user - 2 option (without chat_id)
    # await bot.answer(text=text)

    # Send message to user - 3 option (with reply)
    # await bot.reply(text=text)

    await message.answer(message.text)