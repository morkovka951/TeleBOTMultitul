import telebot
import telegramConnection

from telebot import types


bot = telebot.TeleBot(telegramConnection.telegramConnection)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #useID = message


        # button for user
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Button1")
    item2 = types.KeyboardButton("Button2")
    markup.add(item1,item2)

    bot.send_message(message.chat.id, "Howdy, how are you doing?" , reply_markup=markup)

@bot.message_handler(content_types=['text'])
def getUserText(message):
    bot.send_message(message.chat.id, message)


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.send_message(message.chat_id, message.text)

bot.polling(none_stop=True)

