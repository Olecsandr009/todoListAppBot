import requests
import telebot

SRC = 'http://localhost:3000'

# Button all tasks function
def all_tasks(message, telebot:telebot.TeleBot):
    global bot
    bot = telebot

    tasks = get_all_tasks(message)

# Request get all tasks function
def get_all_tasks(message):
    try:
        response = requests.get(f"{SRC}/task/get-tasks")
        response.raise_for_status()
        all_tasks_list(message, response.json())
    except requests.exceptions.RequestException as error:
        return bot.send_message(message.chat.id, "Невдалося знайти таски")

# Output tasks list function
def all_tasks_list(message, tasks):
    index = 1
    for task in tasks:
        send_message = f"{index}: {task['title']} \n\n {task['text']} \n\n Виконати до: {task['deadline']}"
        bot.send_message(message.chat.id, send_message)
        index = index + 1