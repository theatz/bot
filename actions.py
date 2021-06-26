import telebot
from admins import *

def parse_message(bot, message):
	log(bot, message)

	if message.from_user.id in admins:
		pass
		# bot.reply_to(message, message.text)
		# bot.send_message(message.chat.id, message.chat.id)

def log(bot, message):
	bot.send_message(channel_log_id, message.text + '\n' + str(message.from_user.id) +
					 '\n' + str(message.from_user.first_name))