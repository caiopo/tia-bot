import telegram

start = ('Oi querido, tudo bem? E as namoradinhas? '
			+telegram.Emoji.TWO_HEARTS
			+telegram.Emoji.FACE_THROWING_A_KISS
			+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
			+telegram.Emoji.KISS_MARK)

help = ''

received_image = ('Ai, que lindo! Obrigado, querido. Que deus te abençoe! '
				+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
				+telegram.Emoji.FACE_THROWING_A_KISS
				+telegram.Emoji.KISS_MARK
				+telegram.Emoji.TWO_HEARTS)

unknown_command = 'O que é isso? ' + telegram.Emoji.BLACK_QUESTION_MARK_ORNAMENT

no_cache = ('Não tenho fotos bonitinhas para enviar! Me mande algumas!'
			+telegram.Emoji.KISS_MARK
			+telegram.Emoji.TWO_HEARTS
			+telegram.Emoji.SMILING_FACE_WITH_SMILING_EYES
			+telegram.Emoji.FACE_THROWING_A_KISS)

cache = lambda clen: 'Tenho {} lindas fotos!'.format(clen)

no_image = 'Você não tem nenhuma foto bonita para me mandar?' + telegram.Emoji.BLACK_QUESTION_MARK_ORNAMENT