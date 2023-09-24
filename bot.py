from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv, find_dotenv
from keyboard import kb

load_dotenv(find_dotenv())


bot = Bot(os.getenv(('TOKEN')))
dp = Dispatcher(bot)

st: str = ""
res: float = 0
sign: str = ""
num: str = ""


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    global st
    st = ""
    await message.answer(text="Калькулятор",
                         reply_markup=kb)


@dp.message_handler(lambda message: message.text == '1')
async def calc(message: types.Message):
    global st
    global num
    st += '1'
    num += '1'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '2')
async def calc(message: types.Message):
    global st
    global num
    st += '2'
    num += '2'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '3')
async def calc(message: types.Message):
    global st
    global num
    st += '3'
    num += '3'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '4')
async def calc(message: types.Message):
    global st
    global num
    num += '4'
    st += '4'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '5')
async def calc(message: types.Message):
    global st
    global num
    num += '5'
    st += '5'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '6')
async def calc(message: types.Message):
    global st
    global num
    num += '6'
    st += '6'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '7')
async def calc(message: types.Message):
    global st
    global num
    num += '7'
    st += '7'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '8')
async def calc(message: types.Message):
    global st
    global num
    num += '8'
    st += '8'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '9')
async def calc(message: types.Message):
    global st
    global num
    num += '9'
    st += '9'

    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '0')
async def calc(message: types.Message):
    global st
    global num
    num += '0'
    st += '0'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '.')
async def calc(message: types.Message):
    global st
    global num
    num += '.'
    st += '.'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '+')
async def calc(message: types.Message):
    global st
    global res
    global sign
    global num

    number: str = ""
    for i in st[::-1]:
        if i == " ":
            break
        else:
            number += i
    try:
        res += float(number[::-1])
        st += " + "
        sign = "+"
        num = ""
        await bot.send_message(chat_id=message.from_user.id,
                               text=st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '-')
async def calc(message: types.Message):
    global st
    global res
    global sign
    global num

    number: str = ""
    for i in st[::-1]:
        if i == " ":
            break
        else:
            number += i
    try:
        res += float(number[::-1])
        st += " - "
        sign = "-"
        num = ""
        await bot.send_message(chat_id=message.from_user.id,
                               text=st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '*')
async def calc(message: types.Message):
    global st
    global res
    global sign
    global num

    number: str = ""
    for i in st[::-1]:
        if i == " ":
            break
        else:
            number += i
    try:
        res += float(number[::-1])
        st += " * "
        sign = "*"
        num = ""
        await bot.send_message(chat_id=message.from_user.id,
                               text=st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '/')
async def calc(message: types.Message):
    global st
    global res
    global sign
    global num

    number: str = ""
    for i in st[::-1]:
        if i == " ":
            break
        else:
            number += i
    try:
        res += float(number[::-1])
        st += " / "
        sign = "/"
        num = ""
        await bot.send_message(chat_id=message.from_user.id,
                               text=st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dp.message_handler(lambda message: message.text == '=')
async def calc(message: types.Message):
    global st
    global res
    global sign
    global num
    try:
        if sign == "+":
            res += float(num)
        elif sign == "-":
            res -= float(num)
        elif sign == "*":
            res *= float(num)
        elif sign == "/":
            res /= float(num)

        s = str(res)
        if s[-1] != "0":
            res = float(res)
        else:
            res = int(res)

        await bot.send_message(chat_id=message.from_user.id,
                               text=str(res))
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="На ноль делить нельзя!")
    res = int(res)
    res = 0
    sign = ""
    num = ""
    st = ""


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
