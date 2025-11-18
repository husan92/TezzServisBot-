import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Токенни олиш
TOKEN = os.getenv("BOT_TOKEN").strip()
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start буйруғига жавоб
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Салом! Бот фаол.")

# Асосий функция
async def main():
    await dp.start_polling(bot)

# Агар файл тўғридан-тўғри ишлатилса
if __name__ == "__main__":
    asyncio.run(main())
