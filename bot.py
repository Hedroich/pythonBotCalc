from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

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


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(text="Калькулятор",
                         reply_markup=kb)


@dp.message_handler(lambda message: message.text == '1')
async def calc(message: types.Message):
    global st
    st += '1'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '2')
async def calc(message: types.Message):
    global st
    st += '2'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '3')
async def calc(message: types.Message):
    global st
    st += '3'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '4')
async def calc(message: types.Message):
    global st
    st += '4'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '5')
async def calc(message: types.Message):
    global st
    st += '5'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '6')
async def calc(message: types.Message):
    global st
    st += '6'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '7')
async def calc(message: types.Message):
    global st
    st += '7'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '8')
async def calc(message: types.Message):
    global st
    st += '8'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '9')
async def calc(message: types.Message):
    global st
    st += '9'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '0')
async def calc(message: types.Message):
    global st
    st += '0'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)


@dp.message_handler(lambda message: message.text == '1')
async def calc(message: types.Message):
    global st
    st += '1'
    await bot.send_message(chat_id=message.from_user.id,
                           text=st)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
