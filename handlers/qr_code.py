from io import BytesIO

import qrcode
from aiogram import Router, types
from aiogram.types import BufferedInputFile

qr_code_router = Router()
@qr_code_router.message()
async def qr_code_handler(message: types.Message):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(message.text)
    qr.make(file=True)
    image = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    image.save(buffer, "PNG")
    buffer.seek(0)
    input_file = BufferedInputFile(buffer.getvalue(), filename="qrcode.png")
    await message.answer_photo(photo=input_file)