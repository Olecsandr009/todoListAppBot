import telebot

# Delete task function
def delete(callback, bot:telebot.TeleBot):
    global telebot
    telebot = bot

    bot.delete_message(callback.message.chat.id, callback.message.message_id)