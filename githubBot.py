import telebot
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# Сохранение ответа API в переменной.
response_dict = r.json()
# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
# Анализ первого репозитория.

names, repositorys, desriptions = [], [], []
for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        repositorys.append(repo_dict['html_url'])
        desriptions.append(repo_dict['description'])

# Bot tlg###
bot = telebot.TeleBot('') #@Mobbius_Bot

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'Howdy, how are you doing?')

@bot.message_handler(commands=['python'])
def send_welcome(message):
    #bot.reply_to(message, '???')
    for i in range(3):
        #bot.reply_to(message, names[i])
        bot.reply_to(message, repositorys[i])
        

"""
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,message.text)
"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
        

if __name__ == '__main__':
    bot.polling(none_stop=True)
