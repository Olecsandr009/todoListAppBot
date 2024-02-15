import requests
import json
import telebot

SRC = 'http://localhost:3000'

# Request registration function
def register(message):
    try:
        data = {
            'telegramId': message.from_user.id,
            'name': message.from_user.first_name,
            'firstName': message.from_user.last_name or ""
        }

        response = requests.post(f"{SRC}/user/create-user", data)
        response.raise_for_status()
        return login(message, bot)
    except requests.exceptions.RequestException as error:
        return "error"

# Request login function
def login(message, telebot:telebot.TeleBot):
    global bot
    bot = telebot

    try:
        response = requests.get(f"{SRC}/user/login-user/{message.from_user.id}")
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        return register(message)