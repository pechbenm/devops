import sys
from telebot import TeleBot
from datetime import datetime

token = '8547338296:AAG5ReX6Tlq17mgPfo0pQEl_9Uo8Fa2eV08'
chat_id = '5139109651'
bot = TeleBot(token)
time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def send(prName, version, author):
    message = f"""
    Проект: {prName}
    Версия: {version}
    Дата: {time}
    Владелец: {author}
    """
    bot.send_message(chat_id, message)
    print(f"Сообщение отправлено: {message}")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '123')

if __name__ == '__main__':
    if len(sys.argv) == 4:
        prName = sys.argv[1]
        version = sys.argv[2]
        author = sys.argv[3]
        send(prName, version, author)
    else:
        bot.polling(none_stop=True)