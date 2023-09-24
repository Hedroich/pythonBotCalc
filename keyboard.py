from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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