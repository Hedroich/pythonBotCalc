from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token="6586210550:AAEEH3UAyH1PX0nE59nk0IQ6rAkl2h6vXGI")
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)

k0 = KeyboardButton('0')
k1 = KeyboardButton('1')
k2 = KeyboardButton('2')
k3 = KeyboardButton('3')
k4 = KeyboardButton('4')
k5 = KeyboardButton('5')
k6 = KeyboardButton('6')
k7 = KeyboardButton('7')
k8 = KeyboardButton('8')
k9 = KeyboardButton('9')
k_mult = KeyboardButton('*')
k_div = KeyboardButton('/')
k_res = KeyboardButton('=')
k_plus = KeyboardButton('+')
k_minus = KeyboardButton('-')
k_drop = KeyboardButton('.')

kb.add(k7).insert(k8).insert(k9).insert(k_div)
kb.add(k4).insert(k5).insert(k6).insert(k_mult)
kb.add(k1).insert(k2).insert(k3).insert(k_minus)
kb.add(k0).insert(k_drop).insert(k_plus).insert(k_res)

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
        number = number[::-1]
        if st in '.':
            temp: float = float(number)
        else:
            temp: int = int(number)
        res += temp
        st += " + "
        sign = "+"
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
    if sign == "+":
        res += int(num)
    elif sign == "-":
        res -= num
    elif sign == "*":
        res *= num
    elif sign == "/":
        res /= num

    await bot.send_message(chat_id=message.from_user.id,
                           text=str(res))
    res = 0
    sign = ""
    num = ""
    st = ""

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
