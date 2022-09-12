import telebot
 
token = '5541908250:AAF4jdKBL4lQ2i-2uOGvxLdCd8JGkRJoGcA' # Вставь свой токен
bot = telebot.TeleBot(token)
 
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
 
if __name__ == '__main__':
    bot.polling(none_stop=True)