from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Хэндлер для сообщений, которые не попали в другой хэндлер.
@router.message()
async def send_answer(message: Message):
    await message.answer(LEXICON_RU['other_answer'])
