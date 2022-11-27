import time

import telebot
import random
import checkVisa
import telegramConnection
import botFunction

from telebot import types

def bot():
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

    @bot.message_handler(commands=['visa'])
    def send_welcome(message):
        #useID = message

        #checkVisa.main('OAM-70324-4/ZM-2022')
        #print(checkVisa.statusViza)
        #bot.send_message(message.chat.id, checkVisa.statusViza)
        #time.sleep(3)
        #time.sleep(random.randint(5, 50))
        checkVisa.main('OAM-42474-3/DP-2022')
        print(checkVisa.statusViza)
        bot.send_message(message.chat.id, checkVisa.statusViza)

        # checkVisa.main('OAM-42474-3/DP-2022')
        # print(checkVisa.statusViza)
        # bot.send_message(message.chat.id, checkVisa.statusViza)



    @bot.message_handler(content_types=['text'])
    def getUserText(message):
        print(message.from_user.id)
        idUser = message.from_user.id
        idUser1 = 1999291160    # Alla
        bot.send_message(message.chat.id, message.text)
        #bot.send_message(idUser, message.text)
        #bot.send_message(idUser1, message.text)

    #@bot.message_handler(func=lambda message: True)
    #def echo_all(message):
    #    bot.send_message(message.chat_id, message.text)

    bot.polling(none_stop=True)

