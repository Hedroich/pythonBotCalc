from aiogram import Bot, Dispatcher, types
from aiogram import executor

bot = Bot(token="6586210550:AAEEH3UAyH1PX0nE59nk0IQ6rAkl2h6vXGI")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(messege:types.Message):
    await messege.reply("Привет!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
