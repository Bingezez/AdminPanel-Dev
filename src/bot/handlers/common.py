from aiogram import types, Dispatcher


async def start_message(message: types.Message):
    first_name = '' if message.from_user.first_name \
                        is None else message.from_user.first_name
    last_name = '' if message.from_user.last_name \
                        is None else message.from_user.last_name
    

    await message.answer(
        f"<u>Hi! {first_name} {last_name}</u>\n"
        "Welcome to you in my bot.\n"
        "You need send <b>Special indentification code!</b> "
        "Which you received during registration."
    )


async def help_message(message: types.Message):
    await message.answer("You need write your token.")


async def handler_common(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, commands=['help'])


if __name__ == '__main__':
    pass