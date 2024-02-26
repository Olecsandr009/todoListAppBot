import time
from datetime import datetime, timedelta, date

import telebot
from telebot import types

import schedule

global result_time
global message


def scheduled(deadline, current_message, telebot: telebot.TeleBot, current_task, back):
    global bot
    global task
    global on_back
    bot = telebot
    task = current_task
    on_back = back
    message = current_message

    current_date = str(deadline).split(" ")[0]
    current_time = str(deadline).split(" ")[1]

    result_date = date(*get_current_date(current_date, "-")) - timedelta(days=1)
    result_time = datetime(*(get_current_date(current_date, "-") + get_current_date(current_time, "-"))) - timedelta(days=0, minutes=2)

    # result_time = str(result_time).split(" ")[1]

    # tuple_var = time.struct_time(tuple(get_current_date(str(result_date), "-") + get_current_date(str(result_time), ":") + [0, 0, 0]))

    # schedule.every().day.at(time.strftime("%Y-%m-%d %H-%M-%S", tuple_var)).do(send_scheduled_message(message, task))

    # Schedule message function
    scheduled_time = result_time.strftime("%H:%M")
    schedule_message(scheduled_time, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

def schedule_message(time, message):
    schedule.every().day.at(time).do(send_scheduled_message(message, task))

# Get current date function
def get_current_date(date: str, sep: str):
    current_date = [int(num) for num in date.split(sep)]

    return current_date

# Send scheduled message
def send_scheduled_message(message, task):
    print(task)

    task_message = f"{task['text']}  \n\nВиконати до: {task['deadline']}"

    bot.send_message(message.chat.id, "🚨❗️Виконайте завдання ️❗🚨")
    bot.send_message(message.chat.id, task_message)
    on_back(message)

# On complete function
def on_complete(is_complete):
    if is_complete: return "виконано"
    else: return "не виконано"