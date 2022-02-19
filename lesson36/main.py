import telebot
from telebot import types


bot = telebot.TeleBot("5152711269:AAEGjLKRQGcr9QocKdChoSqo1_ztkOvCfy0")

name=""
surname=""
age=0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.send_message(message.from_user.id, "Привет меня зовут Бот")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    keyword1 = types.InlineKeyboardMarkup()
    button_reg = types.InlineKeyboardButton(text="Регестрация", callback_data="reg")
    button_no1 = types.InlineKeyboardButton(text="Нет", callback_data="no1")
    keyword1.add(button_reg, button_no1)
    if message.text.lower()=="привет":
        bot.send_message(message.from_user.id, text="Привет, давай начнем регистрацию?", reply_markup=keyword1)
    elif message.text=="/reg":
        bot.send_message(message.from_user.id, "Здраствуй, введите ваше имя")
        bot.register_next_step_handler(message, nameReg)

    else:
        bot.send_message(message.from_user.id, "я не понимаю тебя")


def nameReg(message):
    global name
    name=message.text
    bot.send_message(message.from_user.id, "Введите вашу фамилию")
    bot.register_next_step_handler(message, surnameReg)

def surnameReg(message):
    global surname
    surname=message.text
    bot.send_message(message.from_user.id, "Введите ваш возраст цифрами!")
    bot.register_next_step_handler(message, ageReg)

def ageReg(message):
    global age
    while age==0:
        try:
            age=int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Введите возраст цифрами😡")
    keyword=types.InlineKeyboardMarkup()
    button_yes=types.InlineKeyboardButton(text="Да",callback_data="yes")
    button_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyword.add(button_yes,button_no)
    #keyword.add(button_no)
    mess = f"Вас зовут {name} {surname} и ваш возраст {age},верно ли?"
    bot.send_message(message.from_user.id, text=mess, reply_markup=keyword )


@bot.callback_query_handler(func=lambda call: True)
def query_button(call):
    keyword2 = types.InlineKeyboardMarkup()
    button_reg2 = types.InlineKeyboardButton(text="Регистрация(inst)", callback_data="reg2")
    button_no3 = types.InlineKeyboardButton(text="Нет", callback_data="no3")
    keyword2.add(button_reg2, button_no3)
    if call.data=="yes":
        bot.send_message(call.message.chat.id,"Я вас запомнил, через время внесу вас в базу!")
    elif call.data=="no":
        bot.send_message(call.message.chat.id, "Давай попробуем еще раз. Как тебя зовут?")
        bot.register_next_step_handler(call.message, nameReg)
    elif call.data=="reg":
        bot.send_message(call.message.chat.id,"Давайте приступим! Введите ваше имя")
        bot.register_next_step_handler(call.message, nameReg)
    elif call.data=="no1":
        bot.send_message(call.from_user.id, text="Может регистрация instagram?" , reply_markup=keyword2)
    elif call.data=="reg2":
        bot.send_message(call.message.chat.id, "Давайте приступим! Введите ваше имя")
        bot.register_next_step_handler(call.message, nameReg)
    elif call.data=="no3":
        bot.send_message(call.message.chat.id, "Хорошо")


bot.infinity_polling()
