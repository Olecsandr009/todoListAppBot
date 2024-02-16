# 6898764061:AAHR6-ozMhtNh1Wc8ue6iz-iv28xc4QhpM0

import telebot
from telebot import types

from auth.auth import login

from start_buttons.all_tasks import all_tasks
from start_buttons.create_task import create_task

from task.complete.complete import complete
from task.delete.delete import delete

bot = telebot.TeleBot('6898764061:AAHR6-ozMhtNh1Wc8ue6iz-iv28xc4QhpM0')

START_BUTTONS = {
    'all_tasks': 'Всі завдання',
    'create_task': 'Створити завдання',
    'complete_tasks': 'Виконані завдання',
    'urgent_tasks': 'Термінові завдання'
}

BACK_BUTTONS = ["Відмінити", "Назад"]

# Command /start
@bot.message_handler(commands=['start'])
def main(message):
    start(message)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        delete(callback, bot)
    elif callback.data == 'complete':
        complete()
# start function
def start(message):
    markup = types.ReplyKeyboardMarkup(True)
    user = login(message, bot)

    button1 = types.KeyboardButton(START_BUTTONS['all_tasks'])
    button2 = types.KeyboardButton(START_BUTTONS['create_task'])
    button3 = types.KeyboardButton(START_BUTTONS['complete_tasks'])
    button4 = types.KeyboardButton(START_BUTTONS['urgent_tasks'])

    markup.row(button1, button2, button3, button4)

    bot.send_message(message.chat.id, "start")
    bot.send_message(message.chat.id, "Todo List App")
    bot.send_message(message.chat.id, "Що ви хочете побачити",reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

# on_click function
def on_click(message):
    global START_BUTTONS

    if message.text == START_BUTTONS['all_tasks']:
        all_tasks(message, bot, on_back)

    elif message.text == START_BUTTONS['create_task']:
        create_task(message, bot, on_back_btn, on_back)

    elif message.text == START_BUTTONS['complete_tasks']:
        return
    
    elif message.text == START_BUTTONS['urgent_tasks']:
        return

    # bot.register_next_step_handler(message, on_click)

# Back by click the markup
def on_back_btn(message):
    for BUTTON in BACK_BUTTONS:
        if message.text == BUTTON:
            bot.send_message(message.chat.id, "on_back_btn")
            start(message)

# Back by end of action
def on_back(message):
    start(message)

bot.polling(none_stop=True)