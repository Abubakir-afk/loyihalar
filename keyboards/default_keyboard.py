from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telegram Username"),
         KeyboardButton(text="QRCode")],
    ],resize_keyboard=True
)

kb2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga")]
    ], resize_keyboard=True
)