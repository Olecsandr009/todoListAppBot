import requests
import telebot

from telebot import types
from assets import HREF

# Complete task function
def complete_task(message, telebot: telebot.TeleBot, back):
    global bot
    global on_back
    bot = telebot
    on_back = back

    bot.send_message(message.chat.id, "✅Виконанні завдання✅")
    tasks = get_complete_task(message)

# Request get complete task function
def get_complete_task(message):
    try:
        response = requests.get(f"{HREF}/user/get-task-user/{message.from_user.id}")
        response.raise_for_status()
        tasks = response.json()
        complete_task_list(message, tasks)
    except requests.exceptions.RequestException as error:
        bot.send_message(message.chat.id, "🚨Невдалося знайти таски🚨")
        on_back(message)

# Output complete task list
def complete_task_list(message, tasks):
    index = 1

    if bool(tasks[0]["task"]) is False:
        bot.send_message(message.chat.id, "Нажаль ми не знайшли потрібних завдань😔")
        on_back(message)
        return

    for task in tasks[0]["task"]:
        if task["complete"] == False: break
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Видалити", callback_data=f'delete:{task["_id"]}')
        markup.add(button1)

        send_message = f"{index}: {task['title']} \n{task['text']} \n\nСтан: {on_complete(task['complete'])} \n\nВиконати до: {task['deadline']}"
        bot.send_message(message.chat.id, send_message, reply_markup=markup)
        index = index + 1

    on_back(message)

def on_complete(is_complete):
    if is_complete: return "виконано"
    else: return "не виконано"
