# 5113587068:AAFpJRYY7ae68v2fFrLV5hVshKyBt1Jdv7A
import telebot

bot = telebot.TeleBot("5113587068:AAFpJRYY7ae68v2fFrLV5hVshKyBt1Jdv7A", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот 😄")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
  if message.text.lower() == "привет":
    bot.reply_to(message, "Привет!")
  elif message.text.lower() == "как дела?":
    bot.reply_to(message, "Отлично, а у тебя?")
  elif message.text.lower() == "как дела":
    bot.reply_to(message, "Отлично,а у тебя?")
  elif message.text.lower() == "хорошо":
    bot.reply_to(message, "Это круто!")
  elif message.text.lower() == "отлично":
    bot.reply_to(message, "Это круто!")
  elif message.text.lower() == "нормально":
    bot.reply_to(message, "Это хорошо!")
  elif message.text.lower() == "плохо":
      bot.reply_to(message, "Надеюсь, все будет хорошо!🥺")
  elif message.text.lower() == "что делаешь?":
    bot.reply_to(message, "С тобой говорю 😁")
  elif message.text.lower() == "что делаешь":
    bot.reply_to(message, "С тобой говорю 😁")
  elif message.text.lower() == "сколько тебе лет?":
    bot.reply_to(message, "Я был создан 02.02.22 😎.")
  elif message.text.lower() == "сколько тебе лет":
    bot.reply_to(message, "Я был создан 02.02.22 😎.")
  elif message.text.lower() == "пока":
    bot.reply_to(message, "Пока, удачи!")
  #else:
   #bot.reply_to(message, "Я тебя не понимаю😢")
  a = ["ты тупой", "тупой", "ты дурак", "дурак","идиот","ты идиот","лох"]
  for i in a:
    if i == message.text.lower():
      bot.reply_to(message, "Как обзываешься так и сам называешься!😎😉")
bot.infinity_polling()
