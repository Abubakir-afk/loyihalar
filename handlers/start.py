import aiogram
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.default_keyboard import kb

start_router = aiogram.Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Siz botga /start bosdingiz!", reply_markup=kb)