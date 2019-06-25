import telebot
import parser

TOKEN = '569586058:AAEfbf_l6kdTf6r34enTH8ahw1Nv18qbocg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
