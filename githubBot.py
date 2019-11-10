import telebot
from telebot import types
import requests
import githubAPI

# Bot tlg###
bot = telebot.TeleBot('512500856:AAEq_uMUB5omgDPdjuYTGLHw88JphT8TnfA') #@Mobbius_Bot

user_dict = {}

class Git_repos:
    def __init__(self, description):
        self.description = description
        self.count_top = None
        

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
        bot.send_message(message.chat.id, 'Hi!\nВыберите нужны раздел (такой фичи пока нет...)')
        bot.register_next_step_handler(message, desriptions_name)

def desriptions_name(message):
    try:
        chat_id = message.chat.id
        description = message.text
        user = Git_repos(description)
        user_dict[chat_id] = user
        msg = bot.send_message(chat_id, 'Какое колличество репозиториев вывести?')
        bot.register_next_step_handler(msg, top_count_range)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def top_count_range(message):
        try:
                chat_id = message.chat.id
                count_top = message.text
                if not count_top.isdigit():
                        msg = bot.reply_to(message, 'Нужно вести цифру...')
                        bot.register_next_step_handler(message, top_count_range)
                        return
                user = user_dict[chat_id]
                user.count_top = count_top
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                markup.add('python', 'java')
                msg = bot.send_message(chat_id, 'Какой язык программирования?', reply_markup = markup)
                bot.register_next_step_handler(msg, repeat_all_messages)
        except Exception as e:
                bot.send_message(chat_id, 'oooops')

#@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
        try:
                chat_id = message.chat.id
                text = message.text.lower()
                user = user_dict[chat_id]
                if text == 'python':                
                        for i in range(int(user.count_top)):
                                bot.send_message(chat_id, githubAPI.py_names[i] + '\n\n' + githubAPI.py_repositorys[i])
                if text == 'java':
                        for i in range(int(user.count_top)):
                                bot.send_message(chat_id, githubAPI.java_names[i] + '\n\n' + githubAPI.java_repository[i])
        except Exception as e:
                bot.send_message(chat_id, 'oooops')


if __name__ == '__main__':
    bot.polling(none_stop=True)
