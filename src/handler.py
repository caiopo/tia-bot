import telegram
import config
import os
import random
import time

start_text = """
start_text
"""

help_text = """
help text
"""

random.seed()

# Botfather: /setcommands
# help - detailed information about the bot

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
							+telegram.Emoji.FACE_THROWING_A_KISS
							+telegram.Emoji.KISS_MARK
							+telegram.Emoji.TWO_HEARTS)

def help(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=help_text)

def unknown(bot, update):
	if update.message.chat_id > 0: # user	
		bot.sendMessage(chat_id=update.message.chat_id,
						text="Sorry, I didn't understand that command.")

def tia(bot, update):
	clen = _cache_len()

	if clen == 0:
		bot.sendMessage(chat_id=update.message.chat_id,
						text='Não tenho fotos bonitinhas para enviar! Me mande algumas!')
	else:
		try:
			os.listdir(config.CACHE_DIR)

			rnd = random.randrange(0, clen)

			filename = '{cache}/{photo}'.format(cache=config.CACHE_DIR,
												photo=os.listdir(config.CACHE_DIR)[rnd])

			with open(filename, 'rb') as photo:
				bot.sendPhoto(chat_id=update.message.chat_id,
								photo=photo)
		except Exception as e:
			_something_wrong(bot, update, e)
			traceback.print_exc()

def tiarage(bot, update):

	if _cache_len() > 10:
		for i in range(random.randrange(5, 10)):
			tia(bot, update)

def cache(bot, update):

	clen = _cache_len()

	if clen == 0:
		bot.sendMessage(chat_id=update.message.chat_id,
						text='Não tenho fotos bonitinhas para enviar! Me mande algumas!')
	else:
		bot.sendMessage(chat_id=update.message.chat_id,
						text='Tenho {} lindas fotos!'.format(clen))
	
def message(bot, update):
	if update.message.chat_id > 0: # user
		try:
			if not update.message.photo:
				return

			photosize = bot.getFile(update.message.photo[-1].file_id)
	
			filename = '{cache}/photo_{num}.jpg'.format(cache=config.CACHE_DIR,
														num=''.join(str(time.time()).split('.')))

			photosize.download(filename)

			"Ai, que lindo! Obrigado, querido. Que deus te abençoe 😊"

			bot.sendMessage(chat_id=update.message.chat_id,
							text='Ai, que lindo! Obrigado, querido. Que deus te abençoe! '
							+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
							+telegram.Emoji.FACE_THROWING_A_KISS
							+telegram.Emoji.KISS_MARK
							+telegram.Emoji.TWO_HEARTS)

		except Exception as e:
			traceback.print_exc()
			_something_wrong(bot, update, e)


def _cache_len():
	return len(os.listdir(config.CACHE_DIR))


def _something_wrong(bot, update, e):
	bot.sendMessage(chat_id=update.message.chat_id,
					text='Something went wrong...\nError type: {}\nError message: {}'.format(type(e), e))
