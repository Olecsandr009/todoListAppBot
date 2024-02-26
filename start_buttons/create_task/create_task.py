import datetime

import telebot
import requests

from telebot import types
from assets import HREF

from task.deadline.deadline import deadline
from task.scheduled.scheduled import scheduled

current_task = {
    "userId": None,
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

    bot.send_message(message.chat.id, "⬇️Чудово зараз створимо завдання⬇️", reply_markup=markup)
    bot.send_message(message.chat.id, "Введіть назву вашого завдання👀")
    bot.register_next_step_handler(message, get_title)

# Get title function
def get_title(message):
    if on_back_btn(message):return
    current_task["title"] = message.text
    current_task["userId"] = message.from_user.id

    bot.send_message(message.chat.id, "Введіть опис вашого завдання🤓")
    bot.register_next_step_handler(message, get_description)

# Get description function
def get_description(message):
    if on_back_btn(message): return
    current_task["text"] = message.text

    bot.send_message(message.chat.id, "Через яку кількість днів буде дедлайн?🤔")
    bot.register_next_step_handler(message, get_deadline)

# Get deadline function
def get_deadline(message):
    if on_back_btn(message): return
    if str(message.text).isdigit() == False:
        bot.send_message(message.chat.id, "Помилка")
        on_back(message)
        return

    current_date_data = deadline(int(message.text))

    current_date = str(current_date_data).split(" ")[0].split("-")
    current_time = str(current_date_data).split(" ")[1].split(":")

    deadline_date = datetime.datetime(*(int(num) for num in current_date), *(int(num) for num in current_time))
    current_task["deadline"] = deadline_date

    # scheduled(deadline_date, message, bot, current_task, on_back)
    create_task_req(message)

# Request create task function
def create_task_req(message):
    try:
        response = requests.post(f"{HREF}/task/create-task", current_task)
        response.raise_for_status()

        bot.send_message(message.chat.id, "🎉Завдання успішно створене😃")
    except requests.exceptions.RequestException as error:
        bot.send_message(message.chat.id, "🚨Хм. Помилка, спробуйте пізніше😔")
    finally:
        on_back(message)