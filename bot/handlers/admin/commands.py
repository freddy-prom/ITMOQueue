from aiogram import types

import sorting_script
from database import crud
from loader import dp, bot
from view import messages, keyboards
from states.user import UserStates

from config import settings


@dp.message_handler(commands=["run_update"], state="*", user_id=settings.ADMINS_IDS)
async def add_new_subject(message: types.Message):
    await message.answer(messages.STARTED)
    users = crud.get_all_users()
    for user in users:
        try:
            state = dp.current_state(user=user.telegram_id, chat=user.telegram_id)
            await state.reset_data()
            await state.set_state(UserStates.MAIN_MENU)
            await bot.send_message(user.telegram_id, messages.SENDED_TO_MAIN_MENU)
            await bot.send_message(user.telegram_id, messages.IN_MAIN_MENU, reply_markup=keyboards.main_menu)
        except:
            pass
    await message.answer(messages.COMPLITED)


@dp.message_handler(commands=["sort"], state="*", user_id=settings.ADMINS_IDS)
async def sort_queue(message: types.Message):
    await message.answer(messages.STARTED)
    sorting_script.sort_queues()
    await message.answer(messages.COMPLITED)
