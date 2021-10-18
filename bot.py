#импорт нужных элементов и библиотек
import sys
import telebot
from telebot import types, logging
import settings

#добавить базовое логирование
logger = telebot.logger
formatter = logging.Formatter('[%(asctime)s] %(thread)d {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                                  '%m-%d %H:%M:%S')
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)  # or use logging.INFO
ch.setFormatter(formatter)

#назначаем переменную с ключом api бота для связи с серверами Telegram
TOKEN = settings.API_KEY
#создаем бота и передаем ему ключ для авторизации на серверах Telegram
bot = telebot.TeleBot(TOKEN)
#создание message хендлера для обработки команды start
@bot.message_handler(commands=['start'])
def send_welcome(message):
	greet_txt = "Привет, как поживаешь?"
	bot.send_message(message.chat.id, greet_txt)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
#создание conversation хэндлера 
#создание хендлеров для обработки событий
#командуем боту начать ходить в Telegram за сообщениями
#запускаем бота, он будет работать, пока мы его не остановим принудительно
bot.polling()

while True:
    pass
#
#
#