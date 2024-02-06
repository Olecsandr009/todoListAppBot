# 6898764061:AAHR6-ozMhtNh1Wc8ue6iz-iv28xc4QhpM0

import telebot
from telebot import types

bot = telebot.TeleBot('6898764061:AAHR6-ozMhtNh1Wc8ue6iz-iv28xc4QhpM0')

# Приймаємо команду /start
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(True)

    button1 = types.KeyboardButton("Отримати список завдань")
    button2 = types.KeyboardButton("")

    bot.send_message(message.chat.id, "Hello")
    bot.send_message(message.chat.id, "Todo List App")





bot.polling(none_stop=True)