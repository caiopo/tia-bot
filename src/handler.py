import telegram
import config
import os
import random
import time
import responses

random.seed()

# Botfather: /setcommands
# help - sobre titiabot
# tia - envia uma foto linda
# fotos - mostra o número de fotos disponíveis

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=responses.start)

def help(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=responses.help,
					disable_web_page_preview=True)

def unknown(bot, update):
	if update.message.chat_id > 0: # user	
		bot.sendMessage(chat_id=update.message.chat_id,
						text=responses.unknown_command)

def tia(bot, update):
	clen = _cache_len()

	if clen == 0:
		bot.sendMessage(chat_id=update.message.chat_id,
						text=responses.no_cache)
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
						text=responses.no_cache)
	else:
		bot.sendMessage(chat_id=update.message.chat_id,
						text=responses.cache(clen))
	
def message(bot, update):
	if update.message.chat_id > 0: # user
		try:
			if not update.message.photo:
				bot.sendMessage(chat_id=update.message.chat_id,
								text=responses.no_image)
				return

			photosize = bot.getFile(update.message.photo[-1].file_id)
	
			filename = '{cache}/photo_{num}.jpg'.format(cache=config.CACHE_DIR,
														num=''.join(str(time.time()).split('.')))

			photosize.download(filename)

			bot.sendMessage(chat_id=update.message.chat_id,
							text=responses.received_image)

		except Exception as e:
			traceback.print_exc()
			_something_wrong(bot, update, e)


def _cache_len():
	return len(os.listdir(config.CACHE_DIR))


def _something_wrong(bot, update, e):
	bot.sendMessage(chat_id=update.message.chat_id,
					text='Something went wrong...\nError type: {}\nError message: {}'.format(type(e), e))
