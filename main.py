# This is a sample Python script.
import telebot

import botFunction


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def bot():
    bot = telebot.TeleBot("***************************")

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        useID = message

        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.send_message(message.chat_id, message.text)

    bot.polling(none_stop=True)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    botFunction

