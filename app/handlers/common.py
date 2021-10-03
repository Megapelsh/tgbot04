from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.mainmenu import menu
from loader import dp


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Оберіть бажану дію", reply_markup=menu)


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())


async def echo_message(message: types.Message):
    await message.answer(f'User ID: {message.from_user.id}, message is: {message.text}', reply_markup=types.ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, commands="stop", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(echo_message)
