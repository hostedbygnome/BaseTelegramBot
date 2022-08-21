from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Test


# A filter for the /test command, where the status will not be indicated
@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer('You are starting a test.\n'
                         'Question 1.\n\n'
                         'Do you often do meaningless things?')

    # Option first (with function set)
    await Test.Q1.set()

    # Option second (with function first)
    # await Test.first()
    @dp.message_handler(state=Test.Q1)
    async def answer_q1(message: types.Message, state: FSMContext):
        answer = message.text

        # Get the state (Option first)
        # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        # Get the state (Option second) - write via key=var
        await state.update_data(answer1=answer)

        # Option third (pass as a dictionary)
        # await state.update_data(
        #     {
        #         'answer1': answer,
        #     }
        # )

        # Option four (with state.proxy)
        # async with state.proxy() as data:
        #     data['answer1'] = answer
        # Convenient if you need to do data[some_digit] += 1
        # Or data['some_list'].append(1), because no need to first get from the state, and then set it

        await message.answer('Question 2.\n'
                             'Your memory has deteriorated?')
        # await Test.next()
        await Test.Q2.set()

    @dp.message_handler(state=Test.Q2)
    async def answer_q2(message: types.Message, state: FSMContext):
        # Get args
        data = await state.get_data()
        answer1 = data.get('answer1')
        answer2 = message.text

        await message.answer('Thank you for your answers')
        await message.answer(f'Answer 1: {answer1}\n'
                             f'Answer 2: {answer2}')

        # Finish states (Option first)
        # await state.finish()

        # Finish states (Option second)
        # await state.reset_state()

        # Finish states (Option third, without delete data)
        # await state.reset_state(with_data=False)
