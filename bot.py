# bot.py
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer("Салом! Мен ишлаяпман 😊")

async def main():
    try:
        print("Bot ishga tushdi...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
