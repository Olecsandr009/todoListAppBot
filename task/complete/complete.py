import requests
import telebot

SRC = 'http://localhost:3000'

# Request complete task function
def complete(callback, id, telebot:telebot.TeleBot):
    global bot
    bot = telebot

    try:
        response = requests.put(f"{SRC}/task/update-task/{id}")
        response.raise_for_status()
        bot.send_message(callback.message.chat.id, "Завдання виконано")
    except requests.exceptions.RequestException as error:
        bot.send_message(callback.message.chat.id, "Нажаль сталася помилка")