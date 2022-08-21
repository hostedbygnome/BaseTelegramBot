from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

#Custom filter for private chat with bot
class IsPrivate(BoundFilter):

    # The check function is used every time an update comes in and
    # the dispatcher goes through all the filters and handlers used in them.
    # This filter is only used for message_handler and Message type
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE

