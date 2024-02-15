# 6898764061:AAHR6-ozMhtNh1Wc8ue6iz-iv28xc4QhpM0

import telebot
from telebot import types

from auth.auth import login

from start_buttons.all_tasks import all_tasks

bot = telebot.TeleBot('6898764061:AAHR6-ozMhtNh1Wc8ue6iz-iv28xc4QhpM0')

START_BUTTONS = {
    'all_tasks': 'Всі завдання',
    'create_task': 'Створити завдання',
    'complete_tasks': 'Виконані завдання',
    'urgent_tasks': 'Термінові завдання'
}

# Command /start
@bot.message_handler(commands=['start'])
def main(message):
    start(message)

# start function
def start(message):
    markup = types.ReplyKeyboardMarkup(True)
    user = login(message, bot)

    button1 = types.KeyboardButton(START_BUTTONS['all_tasks'])
    button2 = types.KeyboardButton(START_BUTTONS['create_task'])
    button3 = types.KeyboardButton(START_BUTTONS['complete_tasks'])
    button4 = types.KeyboardButton(START_BUTTONS['urgent_tasks'])

    markup.row(button1, button2, button3, button4)

    bot.send_message(message.chat.id, "Todo List App")
    bot.send_message(message.chat.id, "Що ви хочете побачити",reply_markup=markup)


    bot.register_next_step_handler(message, on_click)

# on_click function
def on_click(message):
    global START_BUTTONS

    if message.text == START_BUTTONS['all_tasks']:
        all_tasks(message, bot)

    elif message.text == START_BUTTONS['create_task']:
        return
    elif message.text == START_BUTTONS['complete_tasks']:
        return
    elif message.text == START_BUTTONS['urgent_tasks']:
        return

    bot.register_next_step_handler(message, on_click)

bot.polling(none_stop=True)