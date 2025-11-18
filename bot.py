import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Берём токен из Railway переменной
TOKEN = os.getenv("BOT_TOKEN").strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Привет! Бот работает 😊")

# Ответ на любое сообщение
@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.reply(f"Вы написали: {message.text}")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
