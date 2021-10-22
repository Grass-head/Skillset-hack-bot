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

#создание функций назначающих клавиатуры для последующего вывода в разных хэндлерах
def return_btn():
	main_btn_return = types.ReplyKeyboardMarkup(resize_keyboard=True)
	main_btn_return.add('Вернуться в основное меню')
	return main_btn_return

#def num_keyboard():
	#num_btn = types.InlineKeyboardMarkup()
	#num_btn.add(['1'],['2'],['3'],['4'],['5'])
	#num_btn.add(['6'],['7'],['8'],['9'],['10'])
	#return num_btn

def choice_il_keyboard():
	choice_btn_yes = types.InlineKeyboardButton('Да, веди меня дальше', callback_data = 'choice_yes')
	choice_btn_no = types.InlineKeyboardButton('Нет, хочу вернуться в основное меню', callback_data = 'choice_no')
	choice_kb = types.InlineKeyboardMarkup().add(choice_btn_yes)
	choice_kb.add(choice_btn_no)
	return choice_kb

#создание message хендлера для обработки команды start/приветственные сообщения
@bot.message_handler(commands=['start'])
def send_welcome(message):
	greet_txt = "Привет, соискатель!"
	notion_txt = "Знаешь ли ты, что у тебя уже есть все, чтобы зарабатывать уже завтра? Каждый человек имеет базовый набор навыков, который может заинтересовать работодателя. Сегодня люди зарабатывают самыми разными способами. Даже самые неожиданные умения могут пригодиться. А количество работ, которые можно выполнять не выходя из дома ежедневно растет.  "
	ask_purpose_txt = "Итак, с чем пожаловал? Знаешь свои сильные стороны и хочешь посмотреть профессии, где они выстрелят - введи команду /skill. Если тебя интересует конкретная сфера или профессия, и ты хочешь понять, какие навыки тебе нужны отправь команду /prof."
	bot.send_message(message.chat.id, greet_txt)
	bot.send_message(message.chat.id, notion_txt)
	bot.send_message(message.chat.id, ask_purpose_txt)

#создание функции отлавливающей ввод пользователя и направляющей его на нужную ветку
#ветка SKILL
@bot.message_handler(commands=['skill'])
def skill_input(message):
	txt1 = "Давай уточним информацию? Ты хочешь ввести свои навыки и получить набор релевантных профессий?"
	bot.send_message(message.chat.id, txt1, reply_markup=choice_il_keyboard())

#создание функции отлавливающей ввод пользователя и направляющей его на нужную ветку
#ветка PROFESSION
@bot.message_handler(commands=['prof'])
def prof_input(message):
	txt2 = "Давай уточним информацию? Тебя интересует конкретная сфера или профессия? Ты можешь ввести ключевое слово и получить информацию о навыках, которые тебе пригодятся."
	bot.send_message(message.chat.id, txt2, reply_markup=choice_il_keyboard())


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text, reply_markup=return_btn())

#командуем боту начать ходить в Telegram за сообщениями
#запускаем бота, он будет работать, пока мы его не остановим принудительно
bot.polling()

while True:
    pass
