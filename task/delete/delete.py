import requests
import telebot

SRC = 'http://localhost:3000'

# Delete task function
def delete(callback, id, telebot:telebot.TeleBot):
    global bot
    bot = telebot

    if on_delete(id):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

# Request delete task function
def on_delete(id):
    try:
        response = requests.delete(f"{SRC}/task/delete-task/{id}")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as error:
        return False
