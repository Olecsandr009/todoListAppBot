import telebot
import requests

from telebot import types
from assets import HREF

# Urgent tasks function
def urgent_tasks(message, telebot:telebot.TeleBot, back):
    global bot
    global on_back
    bot = telebot
    on_back = back

    bot.send_message(message.chat.id, "🔔❗️Термінові завдання❗️🔔")
    get_urgent_tasks(message)

# Request get urgent tasks function
def get_urgent_tasks(message):
    try:
        response = requests.get(f"{HREF}/user/get-task-user-date/{message.from_user.id}")
        response.raise_for_status()
        tasks = response.json()
        urgent_tasks_list(message, tasks)
    except requests.exceptions.RequestException as error:
        bot.send_message(message.chat.id, "🚨Невдалося знайти таски🚨")
        on_back(message)


# Output tasks list function
def urgent_tasks_list(message, tasks):
    index = 1

    if bool(tasks) is False:
        bot.send_message(message.chat.id, "Нажаль ми не знайшли потрібних завдань😔")
        on_back(message)
        return

    for task in tasks[0]["task"]:
        if task["complete"] == True: continue
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Виконано", callback_data=f'complete:{task["_id"]}')
        button2 = types.InlineKeyboardButton("Видалити", callback_data=f'delete:{task["_id"]}')
        markup.add(button1, button2)

        send_message = f"{index}: {task['title']} \n{task['text']} \n\nСтан: {on_complete(task['complete'])} \n\nВиконати до: {task['deadline']}"
        bot.send_message(message.chat.id, send_message, reply_markup=markup)
        index = index + 1

    on_back(message)

# On_complete function
def on_complete(is_complete):
    if is_complete: return "виконано"
    else: return "не виконано"