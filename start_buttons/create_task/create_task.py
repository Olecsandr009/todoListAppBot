import datetime

import telebot
import requests
from telebot import types

SRC = 'http://localhost:3000'

current_task = {
    "title": None,
    "text": "",
    "deadline": 0
}

# Create task function
def create_task(message, telebot:telebot.TeleBot, back_btn, back):
    global bot
    global on_back_btn
    global on_back
    bot = telebot
    on_back_btn = back_btn
    on_back = back

    markup = types.ReplyKeyboardMarkup(True)
    button = types.KeyboardButton("Відмінити")
    markup.add(button)

    bot.send_message(message.chat.id, "Чудово зараз створимо завдання", reply_markup=markup)
    bot.send_message(message.chat.id, "Введіть назву вашого завдання")
    bot.register_next_step_handler(message, get_title)

# Get title function
def get_title(message):
    if on_back_btn(message):return
    current_task["title"] = message.text

    bot.send_message(message.chat.id, "Введіть опис вашого завдання")
    bot.register_next_step_handler(message, get_description)

# Get description function
def get_description(message):
    if on_back_btn(message): return
    current_task["text"] = message.text

    bot.send_message(message.chat.id, "Через яку кількість днів буде дедлайн?")
    bot.register_next_step_handler(message, get_deadline)

# Get deadline function
def get_deadline(message):
    if on_back_btn(message): return
    current_task["deadline"] = message.text
    create_task_req(message)

# Request create task function
def create_task_req(message):
    try:
        response = requests.post(f"{SRC}/task/create-task", current_task)
        response.raise_for_status()

        bot.send_message(message.chat.id, "Завдання успішно створене")
    except requests.exceptions.RequestException as error:
        bot.send_message(message.chat.id, "Хм. Помилка, спробуйте пізніше")
    finally:
        on_back(message)