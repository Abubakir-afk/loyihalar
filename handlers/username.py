from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.default_keyboard import kb2, kb
from states.state import GetUsername

username_router = Router()

@username_router.message(F.text == "Telegram Username")
async def get_username(msg: Message, state: FSMContext):
    await msg.answer("Nomeringizni kiriting:", reply_markup=kb2)
    await state.set_state(GetUsername.confirm)

@username_router.message(StateFilter("*"), F.text == "Orqaga")
async def get_username(msg: Message, state: FSMContext):
    await msg.answer("Siz menu-ga qaytingiz!", reply_markup=kb)
    await state.clear()

@username_router.message(StateFilter(GetUsername.confirm), F.text.startswith("+998"))
async def get_username(msg: Message, state: FSMContext):
    await msg.answer(f"https://t.me/{msg.text}", reply_markup=kb2)
    await state.set_state(GetUsername.confirm)