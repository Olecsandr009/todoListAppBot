import telebot
from telebot import types

from auth.auth import login

from start_buttons.all_tasks.all_tasks import all_tasks
from start_buttons.create_task.create_task import create_task
from start_buttons.complete_task.complete_task import complete_task
from start_buttons.urgent_tasks.urgent_tasks import urgent_tasks

from task.complete.complete import complete
from task.delete.delete import delete
from assets import TOKEN

bot = telebot.TeleBot(TOKEN)

START_BUTTONS = {
    'all_tasks': 'Завдання',
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
    if callback.data.split(':')[0] == 'delete':
        id = callback.data.split(':')[1]
        delete(callback, id, bot)
    elif callback.data.split(':')[0] == 'complete':
        id = callback.data.split(':')[1]
        complete(callback, id, bot)
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
        all_tasks(message, bot, on_back)

    elif message.text == START_BUTTONS['create_task']:
        create_task(message, bot, on_back_btn, on_back)

    elif message.text == START_BUTTONS['complete_tasks']:
        complete_task(message, bot, on_back)
    
    elif message.text == START_BUTTONS['urgent_tasks']:
        urgent_tasks(message, bot, on_back)

# Back by click the markup
def on_back_btn(message):
    for BUTTON in BACK_BUTTONS:
        if message.text == BUTTON:
            start(message)
            return True

# Back by end of action
def on_back(message):
    start(message)

bot.polling(none_stop=True)