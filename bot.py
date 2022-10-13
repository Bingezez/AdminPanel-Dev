import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.bot.handlers.common import handler_common
from src.bot.handlers.verification import handler_verification


async def main():
    token = '1563593697:AAFZdBEXhQrlzv_TvIpCug2g1kRj2rmcBhM'

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", 
    )

    logger = logging.getLogger(__name__)
    logger.error("Starting bot")

    bot = Bot(token=token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=MemoryStorage())

    await handler_common(dp)
    await handler_verification(dp)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
