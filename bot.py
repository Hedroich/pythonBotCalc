from aiogram import Bot, Dispatcher, types, executor
import os
from dotenv import load_dotenv, find_dotenv
from keyboard import kb
from click import Click
from calc import Calc

load_dotenv(find_dotenv())

cl = Click()
calculator = Calc()

bot = Bot(os.getenv(('TOKEN')))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    cl.clean_all()
    await message.answer(text="Калькулятор",
                         reply_markup=kb)


@dp.message_handler(lambda message: message.text == '1')
async def calc(message: types.Message):
    cl.click_num("1", "1")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '2')
async def calc(message: types.Message):
    cl.click_num("2", "2")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)

@dp.message_handler(lambda message: message.text == '3')
async def calc(message: types.Message):
    cl.click_num("3", "3")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '4')
async def calc(message: types.Message):
    cl.click_num("4", "4")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '5')
async def calc(message: types.Message):
    cl.click_num("5", "5")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '6')
async def calc(message: types.Message):
    cl.click_num("6", "6")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '7')
async def calc(message: types.Message):
    cl.click_num("7", "7")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '8')
async def calc(message: types.Message):
    cl.click_num("8", "8")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '9')
async def calc(message: types.Message):
    cl.click_num("9", "9")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '0')
async def calc(message: types.Message):
    cl.click_num("0", "0")
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.st)


@dp.message_handler(lambda message: message.text == '.')
async def calc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=cl.click_num(".", "."))


@dp.message_handler(lambda message: message.text == '+')
async def calc(message: types.Message):
    try:
        # calculator.res = calculator.result(cl.num, calculator.sign)
        calculator.summa(cl.st, "+")
        cl.set_st("+")
        calculator.set_sing("+")
        cl.clean_num()

        await bot.send_message(chat_id=message.from_user.id,
                               text=cl.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '-')
async def calc(message: types.Message):
    try:
        # calculator.res = calculator.result(cl.num, calculator.sign)
        calculator.summa(cl.st, "-")
        cl.set_st("-")
        calculator.set_sing("-")
        cl.clean_num()
        await bot.send_message(chat_id=message.from_user.id,
                               text=cl.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '*')
async def calc(message: types.Message):
    try:
        calculator.summa(cl.st, "*")
        cl.set_st("*")
        calculator.set_sing("*")
        cl.clean_num()
        await bot.send_message(chat_id=message.from_user.id,
                               text=cl.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '/')
async def calc(message: types.Message):
    try:
        calculator.summa(cl.st, "/")
        cl.set_st("/")
        calculator.set_sing("/")
        cl.clean_num()
        await bot.send_message(chat_id=message.from_user.id,
                               text=cl.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '=')
async def calc(message: types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text=str(calculator.result(cl.num, calculator.sign)))
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="На ноль делить нельзя!")
    finally:
        calculator.clean_res()
        cl.clean_all()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
