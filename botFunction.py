import telebot
import telegramConnection


bot = telebot.TeleBot(telegramConnection.telegramConnection)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    useID = message

    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat_id, message.text)

bot.polling(none_stop=True)
