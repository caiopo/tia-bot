import telegram
import config
import os
import praw
import random

hello_text = """
hello_text
"""

help_text = """
help text
"""

random.seed()


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

	clen = _cache_len()

	if clen == 0:
		bot.sendMessage(chat_id=update.message.chat_id,
				text='Não tenho fotos bonitinhas para enviar! Me mande algumas!')

	rnd = random.randint(0, clen)

	with open('{cache}/{photonum}.jpg'.format(config.CACHE_DIR, rnd), 'rb') as photo:
		bot.sendMessage(chat_id=update.message.chat_id,
						photo=photo)


def unknown(bot, update):
	if update.message.chat_id > 0: # user	
		bot.sendMessage(chat_id=update.message.chat_id,
						text="Sorry, I didn't understand that command.")


def message(bot, update):
	if not update.message.photo:
		return

	photosize = bot.getFile(update.message.photo[-1].file_id)

	photosize.download(str(_cache_len()) + '.jpg')



def _cache_len():
	return len(os.listdir(config.CACHE_DIR))


def _something_wrong(bot, update, e):
	bot.sendMessage(chat_id=update.message.chat_id,
					text='Something went wrong...\nError type: {}\nError message: {}'.format(type(e), e))
