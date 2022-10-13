from argparse import Action
from locale import currency
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ReplyKeyboardMarkup, \
#     KeyboardButton

from ...database.account import AccountDb
from ..utils import random_code


class Verification(StatesGroup):
    token = State()
    username = State()


async def start_verification(message: types.Message):
    await Verification.token.set()
    await message.answer("Load your Token!")
    
    
async def load_token(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['token'] = message.text
    
    await Verification.next()
    await message.answer(
        "Please write your username or phone number.\n"
        "<u>When you registered, you entered data about Telegram.</u>"
    )

async def load_info_about_user(message: types.Message, state: FSMContext):
    code = random_code()
    db = AccountDb()
    async with state.proxy() as data:
        data['username'] = message.text
    current_state = await state.get_data()
    token = current_state['token']
    username = current_state['username']
    if db.is_account(token, username):
        if db.is_code(token, username):
            db.update_account(token, username, code)
        await message.answer(f"Your code is <code>{db.get_code(token, username)}</code>.")
    else:
        await message.answer('What went wrong!')
    
    await state.finish()

    

async def handler_verification(dp: Dispatcher):
    dp.register_message_handler(start_verification, commands=['verification'], state=None)
    dp.register_message_handler(load_token, state=Verification.token)
    dp.register_message_handler(load_info_about_user, state=Verification.username)


if __name__ == '__main__':
    pass
