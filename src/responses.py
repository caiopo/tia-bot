import telegram

start = ('Oi querido, tudo bem? E as namoradinhas? '
			+telegram.Emoji.TWO_HEARTS
			+telegram.Emoji.FACE_THROWING_A_KISS
			+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
			+telegram.Emoji.KISS_MARK)

help = """Eu sou a Titia Bot e tenho muitas fotos lindas para mandar no grupo da familia! {}

Mande /tia ou /titia e eu enviarei uma foto para você! {}

Você também pode me mandar fotos lindas por mensagem privada e eu passarei a enviar elas também! {} {}

Meu repositório: https://github.com/caiopo/tia-bot
""".format(telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES,
			telegram.Emoji.FACE_THROWING_A_KISS,
			telegram.Emoji.KISSING_FACE,
			telegram.Emoji.SMILING_FACE_WITH_HEART_SHAPED_EYES)

received_image = ('Ai, que lindo! Obrigada, querido. Que deus te abençoe! '
				+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
				+telegram.Emoji.FACE_THROWING_A_KISS
				+telegram.Emoji.KISS_MARK
				+telegram.Emoji.TWO_HEARTS)

contributions_disabled = telegram.Emoji.FACE_THROWING_A_KISS * 3

unknown_command = 'O que é isso? ' + telegram.Emoji.BLACK_QUESTION_MARK_ORNAMENT

no_cache = ('Não tenho fotos para enviar! Me mande algumas!'
			+telegram.Emoji.KISS_MARK
			+telegram.Emoji.TWO_HEARTS
			+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
			+telegram.Emoji.FACE_THROWING_A_KISS)

cache = lambda clen: 'Tenho {} lindas fotos!'.format(clen)

no_image = 'Você não tem nenhuma foto bonita para me mandar?' + telegram.Emoji.BLACK_QUESTION_MARK_ORNAMENT

activate_auto_msg = ('Agora vou mandar fotos lindas para você de vez em quando!'
					+telegram.Emoji.KISS_MARK
					+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
					+telegram.Emoji.TWO_HEARTS
					+telegram.Emoji.FACE_THROWING_A_KISS)

deactivate_auto_msg = 'desativado'