from aiogram.fsm.state import StatesGroup, State


class GetUsername(StatesGroup):
    confirm = State()