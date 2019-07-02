import telebot
import requests

py_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
java_url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'

#python#
py_r = requests.get(py_url)
# Сохранение ответа API в переменной.
py_response_dict = py_r.json()
# Анализ информации о репозиториях.
py_repo_dicts = py_response_dict['items']
# Анализ первого репозитория.

py_names, py_repositorys, py_desriptions = [], [], []
for py_repo_dict in py_repo_dicts:
        py_names.append(py_repo_dict['name'])
        py_repositorys.append(py_repo_dict['html_url'])
        py_desriptions.append(py_repo_dict['description'])

#java#
java_r = requests.get(java_url)
java_response_dict =java_r.json()
java_repo_dicts = java_response_dict['items']

java_names, java_repository, java_desriptions = [], [], []
for java_repo_dict in java_repo_dicts:
        java_names.append(java_repo_dict['name'])
        java_repository.append(java_repo_dict['html_url'])
        java_desriptions.append(java_repo_dict['description'])

# Bot tlg###
bot = telebot.TeleBot('') #@Mobbius_Bot

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
        bot.send_message(message.chat.id, 'Hi!\nВыберите нужны раздел (такой фичи пока нет...)')
        

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
        #chat_id = message.chat.id
        text = message.text.lower()
        if text == 'python':
                bot.register_next_step_handler(message, send_py)
        if text == 'java':
                bot.register_next_step_handler(message, send_java)

#@bot.message_handler(commands=['python'])
def send_py(message):
        chat_id = message.chat.id
        text = message.text.lower()
        #print(text)
        for i in range(4):
                #bot.reply_to(message, names[i])
                bot.send_message(chat_id, py_repositorys[i])

#@bot.message_handler(commands=['java'])
def send_java(message):
        chat_id = message.chat.id
        text = message.text.lower()
        for i in range(3):
                bot.send_message(chat_id, java_repository[i])        


if __name__ == '__main__':
    bot.polling(none_stop=True)
