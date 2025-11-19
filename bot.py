import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # 2.x версиясида шундай импорт қилиш керак

TOKEN = os.getenv("BOT_TOKEN").strip()  # токенни муҳит ўзгарувчисидан олиш
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# /start буйруғига жавоб
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Салом! Бот фаол.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
