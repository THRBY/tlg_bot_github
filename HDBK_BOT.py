import telebot
import parser

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'привет':
        bot.send_message(chat_id, 'Привет, я бот - парсер хабра.')
    elif text == 'как дела?':
        bot.send_message(chat_id, 'Лушче всех!')
    else:
        bot.send_message(chat_id, 'Шо?')

if __name__ == '__main__':
    bot.polling(none_stop=True)
