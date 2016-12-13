import telebot
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=['saludo'])
def hello(message):
	name = message.from_user.username
	bot.reply_to(message, "Buenas " + name)

# @bot.message_handler(commands=[''

print("runing...")
bot.polling()
