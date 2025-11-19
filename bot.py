import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = "SENING_BOT_TOKENING"

# Бот ва диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# /start буйруғи
@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer("Salom! Bot ishga tushdi ✅")

# Асосий цикл
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
