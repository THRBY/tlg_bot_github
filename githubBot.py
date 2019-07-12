import telebot
import requests
import githubAPI

# Bot tlg###
bot = telebot.TeleBot('512500856:AAEq_uMUB5omgDPdjuYTGLHw88JphT8TnfA') #@Mobbius_Bot

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
                bot.send_message(chat_id, githubAPI.py_desriptions[i])
                bot.send_message(chat_id, githubAPI.py_repositorys[i])

#@bot.message_handler(commands=['java'])
def send_java(message):
        chat_id = message.chat.id
        text = message.text.lower()
        for i in range(3):
                bot.send_message(chat_id, githubAPI.java_desriptions[i])
                bot.send_message(chat_id, githubAPI.java_repository[i])        


if __name__ == '__main__':
    bot.polling(none_stop=True)
