import telegram
import config
import os
import praw

hello_text = """
hello_text
"""

help_text = """
help text
"""

# Botfather: /setcommands
# help - detailed information about the bot

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=hello_text+'\n\n'+help_text,
					parse_mode=telegram.ParseMode.MARKDOWN,
					disable_web_page_preview=True)

def help(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=help_text,
					parse_mode=telegram.ParseMode.MARKDOWN,
					disable_web_page_preview=True)

def tia(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text="placeholder")


def unknown(bot, update):
	if update.message.chat_id > 0: # user	
		bot.sendMessage(chat_id=update.message.chat_id,
						text="Sorry, I didn't understand that command.")


def message(bot, update):
	pass

def _something_wrong(bot, update, e):
	bot.sendMessage(chat_id=update.message.chat_id,
					text='Something went wrong...\nError type: {}\nError message: {}'.format(type(e), e))
