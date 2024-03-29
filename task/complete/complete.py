import requests
import telebot

from assets import HREF

# Complete task function
def complete(callback, id, telebot:telebot.TeleBot):
    global bot
    bot = telebot

    if on_complete(id):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

# Request on complete task junction
def on_complete(id):
    try:
        response = requests.put(f"{HREF}/task/update-task/{id}")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as error:
        return False