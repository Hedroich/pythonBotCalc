from aiogram import Bot, Dispatcher, types, executor
import os
from dotenv import load_dotenv, find_dotenv
from keyboard import kb
from click import Click
from calc import Calc

load_dotenv(find_dotenv())

click_in_bot = Click()
calculator = Calc()

bot = Bot(os.getenv(('TOKEN')))
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    click_in_bot.clean_all()
    await message.answer(text="Калькулятор",
                         reply_markup=kb)


@dispatcher.message_handler(lambda message: message.text == '1')
async def calc(message: types.Message):
    click_in_bot.click_num("1", "1")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '2')
async def calc(message: types.Message):
    click_in_bot.click_num("2", "2")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)

@dispatcher.message_handler(lambda message: message.text == '3')
async def calc(message: types.Message):
    click_in_bot.click_num("3", "3")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '4')
async def calc(message: types.Message):
    click_in_bot.click_num("4", "4")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '5')
async def calc(message: types.Message):
    click_in_bot.click_num("5", "5")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '6')
async def calc(message: types.Message):
    click_in_bot.click_num("6", "6")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '7')
async def calc(message: types.Message):
    click_in_bot.click_num("7", "7")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '8')
async def calc(message: types.Message):
    click_in_bot.click_num("8", "8")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '9')
async def calc(message: types.Message):
    click_in_bot.click_num("9", "9")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '0')
async def calc(message: types.Message):
    click_in_bot.click_num("0", "0")
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.st)


@dispatcher.message_handler(lambda message: message.text == '.')
async def calc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=click_in_bot.click_num(".", "."))


@dispatcher.message_handler(lambda message: message.text == '+')
async def calc(message: types.Message):
    try:
        # calculator.res = calculator.result(cl.num, calculator.sign)
        calculator.summa(click_in_bot.st, "+")
        click_in_bot.set_st("+")
        calculator.set_sing("+")
        click_in_bot.clean_num()

        await bot.send_message(chat_id=message.from_user.id,
                               text=click_in_bot.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dispatcher.message_handler(lambda message: message.text == '-')
async def calc(message: types.Message):
    try:
        # calculator.res = calculator.result(cl.num, calculator.sign)
        calculator.summa(click_in_bot.st, "-")
        click_in_bot.set_st("-")
        calculator.set_sing("-")
        click_in_bot.clean_num()
        await bot.send_message(chat_id=message.from_user.id,
                               text=click_in_bot.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dispatcher.message_handler(lambda message: message.text == '*')
async def calc(message: types.Message):
    try:
        calculator.summa(click_in_bot.st, "*")
        click_in_bot.set_st("*")
        calculator.set_sing("*")
        click_in_bot.clean_num()
        await bot.send_message(chat_id=message.from_user.id,
                               text=click_in_bot.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dispatcher.message_handler(lambda message: message.text == '/')
async def calc(message: types.Message):
    try:
        calculator.summa(click_in_bot.st, "/")
        click_in_bot.set_st("/")
        calculator.set_sing("/")
        click_in_bot.clean_num()
        await bot.send_message(chat_id=message.from_user.id,
                               text=click_in_bot.st)
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Введите число")


@dispatcher.message_handler(lambda message: message.text == '=')
async def calc(message: types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text=str(calculator.result(click_in_bot.num, calculator.sign)))
    except:
        await bot.send_message(chat_id=message.from_user.id,
                               text="На ноль делить нельзя!")
    finally:
        calculator.clean_res()
        click_in_bot.clean_all()


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
