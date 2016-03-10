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

AUTO_MSG_TIME = [9, 14, 18] # Hour

def init():
	global auto_msg_targets

	auto_msg_targets = _start_auto_msg()

	print(auto_msg_targets)

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
	if _cache_len() > 15:
		for _ in range(random.randrange(10, 15)):
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

def ativar(bot, update):
	if update.message.chat_id not in auto_msg_targets:
		auto_msg_targets.append(update.message.chat_id)
		_save_auto_msg()
		bot.sendMessage(chat_id=update.message.chat_id,
						text=responses.activate_auto_msg)

def desativar(bot, update):
	if update.message.chat_id in auto_msg_targets:
		auto_msg_targets.remove(update.message.chat_id)
		_save_auto_msg()
		bot.sendMessage(chat_id=update.message.chat_id,
						text=responses.deactivate_auto_msg)


def auto_msg_job(bot):
	timenow = time.localtime()

	# sum 2 to correct the time difference between the cloud server and the real UTC-3
	if (timenow.tm_hour + 2) in AUTO_MSG_TIME and timenow.tm_min == 0:
		for chat_id in auto_msg_targets:
			try:
				rnd = random.randrange(0, _cache_len())

				filename = '{cache}/{photo}'.format(cache=config.CACHE_DIR,
													photo=os.listdir(config.CACHE_DIR)[rnd])

				with open(filename, 'rb') as photo:
					bot.sendPhoto(chat_id=chat_id,
									photo=photo)
			except Exception as e:
				traceback.print_exc()


def _start_auto_msg():
	try:
		with open('automsg.txt') as targets:
			return [int(chat_id) for chat_id.strip('\n') in targets]
	except FileNotFoundError:
		open('automsg.txt', 'w').close()
		return []

def _save_auto_msg():
	with open('automsg.txt', 'w') as targets:
		for chat_id in auto_msg_targets:
			targets.write(str(chat_id)+'\n')

def _cache_len():
	return len(os.listdir(config.CACHE_DIR))


def _something_wrong(bot, update, e):
	bot.sendMessage(chat_id=update.message.chat_id,
					text='Something went wrong...\nError type: {}\nError message: {}'.format(type(e), e))


init()