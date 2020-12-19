import telebot

bot = telebot.TeleBot('1412005435:AAFbs3EVuTxJhszv-vUP7oDrpl7gzCOuMdY')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/help')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('/go')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('a', 'b', 'c')

coopybook = {
    'b': 'Правильно',
    'привет': 'Привет',
    'пока': 'Пока',
    'text': 'Я тебя не понимаю'
}


@bot.message_handler(commands=['start'])
def start_start(start):
    bot.send_message(start.chat.id, 'Привет, приятно познакомиться', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def start_help(help):
    bot.send_message(help.chat.id, 'Привет, я пришел тебе на помощь, вот список моих команд:')
    bot.send_message(help.chat.id, '\n /help - список команд.'
                                   '\n /start - проверить мой пульс.'
                                   '\n /Christmas - поздравить с Новым Годом!'
                                   '\n /update - последнее обновление бота'
                                   '\n /play - поиграть с ботом')


@bot.message_handler(commands=['Christmas'])
def start_Christmas(Christmas):
    bot.send_sticker(Christmas.chat.id, 'CAACAgEAAxkBAAEBrIpf1Jbm4DiLPnRCebSVBR38vRZt8AACJAkAAr-MkAQRaBNy67Aybh4E')


@bot.message_handler(commands=['update'])
def start_update(update):
    bot.send_message(update.chat.id, 'Добавлена игра (/play)\n(Еще в разработке)')


@bot.message_handler(commands=['play'])
def start_play(play):
    bot.send_message(play.chat.id, 'Привиет, давай поиграем в игру "Отгадай значение"', reply_markup=keyboard2)


@bot.message_handler(commands=['go'])
def start_go(go):
    bot.send_message(go.chat.id, 'Что такое "Канитель"?\n a. Суета, излишняя торопливость'
                                 '\n b. Металлическая нить для вышивания\n c. Сильный морской ветер',
                     reply_markup=keyboard3)





@bot.message_handler(content_types=['text'])
def start_message(message):
    print(message)
    name = coopybook.get(message.text.lower())
    print(name)
    if message.text.lower() == 'c':
        bot.send_message(message.from_user.id,'\nНеправильно\nЧто такое "Канитель"?\n a. Суета, излишняя торопливость \
                         \n b. Металлическая нить для вышивания\n c. Сильный морской ветер', reply_markup=keyboard3)
    elif message.text.lower() == 'a':
        bot.send_message(message.from_user.id,'\nНеправильно\nЧто такое "Канитель"?\n a. Суета, излишняя торопливость \
                         \n b. Металлическая нить для вышивания\n c. Сильный морской ветер', reply_markup=keyboard3)
    if name:
        bot.send_message(message.from_user.id, name)
 #   if ff.text.lower() == 'b':
 #       bot.send_message(ff.from_user.id, "Правильно")
 #   elif ff.text.lower() == 'a':
 #       bot.send_message(ff.from_user.id, "Не правильно\nПопробуй еще")
 #       bot.send_message(ff.chat.id, 'Что такое "Канитель"?\n a. Суета, излишняя торопливость'
 #                                    '\n b. Металлическая нить для вышивания\n c. Сильный морской ветер',
 #                        reply_markup=keyboard3)
 #   elif ff.text.lower() == 'c':
 #       bot.send_message(ff.from_user.id, "Не правильно\nПопробуй еще")
 #       bot.send_message(ff.chat.id, 'Что такое "Канитель"?\n a. Суета, излишняя торопливость'
 #                                    '\n b. Металлическая нить для вышивания\n c. Сильный морской ветер',
 #                        reply_markup=keyboard3)
 #   elif message.text.lower() == 'привет':
 #       bot.send_message(message.from_user.id, "Привет")
 #   elif message.text.lower() == 'пока':
 #       bot.send_message(message.from_user.id, "Пока")
 #   elif message.text.lower() == 'hello':
 #       bot.send_message(message.from_user.id, "Hello")
 #   elif message.text.lower() == 'goodbye':
 #       bot.send_message(message.from_user.id, "Goodbye")
 #
 #   else:
 #       bot.send_message(message.from_user.id, "Я тебя не понимаю")


@bot.message_handler(content_types=['sticker'])
def sticker_id(sticker):
    print(sticker)


bot.polling(none_stop=True, interval=0)
