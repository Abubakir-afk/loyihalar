import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import command
from dotenv import load_dotenv

from handlers.start import start_router
from handlers.username import username_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(username_router)
# @dp.message()
# async def menu_handler(message: types.Message):
#     await message.answer(text=f"https://t.me/{message.text}")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())