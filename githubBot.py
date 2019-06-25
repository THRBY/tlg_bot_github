import telebot
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# Сохранение ответа API в переменной.
response_dict = r.json()
# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
# Анализ первого репозитория.
"""
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
"""
# Bot tlg###
bot = telebot.TeleBot('407733759:AAE3dU8zVQLwnrMZv2zrdStGCPYJHy4hb_I')

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'Howdy, how are you doing?')

@bot.message_handler(commands=['python'])
def send_welcome(message):
    #bot.reply_to(message, '???')
    bot.reply_to(message, "Selected information about first repository:")
    for repo_dict in repo_dicts:
        bot.reply_to(message, repo_dict['name'])
        """
        bot.reply_to(message, 'Owner:', repo_dict['owner']['login'])
        bot.reply_to(message, 'Stars:', repo_dict['stargazers_count'])
        bot.reply_to(message, 'Repository:', repo_dict['html_url'])
        bot.reply_to(message,'Created:', repo_dict['created_at'])
        bot.reply_to(message, 'Updated:', repo_dict['updated_at'])
        bot.reply_to(message, 'Description:', repo_dict['description'])
        """


"""
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,message.text)
"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
    if message.chat.type == 'python':
        bot.reply_to(message,'...')

if __name__ == '__main__':
    bot.polling(none_stop=True)
