import telebot
from actions import *
import logging

bot = telebot.TeleBot("1809502281:AAGoXKarZfcbhKM5YAXXVTfa612ML85J87I", num_threads=3)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
	parse_message(bot, message)

# @bot.channel_post_handler()
# def channel_hadnlder(message):
# 	bot.send_message(message.chat.id, message.chat.id)

bot.polling()