import logging

from aiogram.types import Update

from loader import dp


@dp.errors_handlers()
async def error_handler(update, exception):
    '''
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return stdout logging:
    '''
    from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                          CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                          MessageTextIsEmpty, RetryAfter, CantParseEntities,
                                          MessageCantBeDeleted, BadRequest)

    if isinstance(exception, Unauthorized):
        logging.info(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f'InvalidQueryID: {exception}\nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception}\nUpdate: {update}')
        return True

    if isinstance(exception, CantDemoteChatCreator):
        logging.debug('Can not demote chat creator')
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug('Message is not modified')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.info('Message to delete is not found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('Message text is empty')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception}\nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        await Update.get_current().message.answer(f'Cant parse entities: {exception.args}')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.info('Message can not be deleted')
        return True

    if isinstance(exception, BadRequest):
        logging.exception(f'BadRequest: {exception}\nUpdate: {update}')
        return True

    logging.exception(f'Update: {update}\n{exception}')
