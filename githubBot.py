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
        self.language = None


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
        bot.send_message(message.chat.id, 'Hi!\nВыберите нужны раздел. Нужно английском')
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
                
                #markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                #markup.add('python', 'java')                
                #msg = bot.send_message(chat_id, 'Какой язык программирования?', reply_markup = markup)

                msg = bot.send_message(chat_id, 'Ведите язык программирования?')
                bot.register_next_step_handler(msg, send_programming_language)                
        except Exception as e:
                bot.send_message(chat_id, 'oooops')


def send_programming_language(message):
        try:
                chat_id = message.chat.id
                language = message.text.lower()
                user = user_dict[chat_id]
                user.language = language
                   
                language_url = 'https://api.github.com/search/repositories'
                lang = user.language
                descrip = user.description
                
                #pad = {'q':'language:%s' %lang}
                pad = {'q': '{0}:{1}'.format(descrip, lang)}
                work_url = requests.get(language_url, params = pad)             
                
                language_response_dict = work_url.json()
                language_repo_dicts = language_response_dict['items']

                language_names, language_repositorys, language_desriptions = [], [], []

                for language_repo_dict in language_repo_dicts:
                        language_names.append(language_repo_dict['name'])
                        language_repositorys.append(language_repo_dict['html_url'])
                        language_desriptions.append(language_repo_dict['description'])
                
                for i in range(int(user.count_top)):
                                bot.send_message(chat_id, language_names[i] + '\n\n' + language_repositorys[i])

                
        except Exception as e:
                bot.send_message(chat_id, 'oooops')

if __name__ == '__main__':
    bot.polling(none_stop=True)
