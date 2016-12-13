import telebot
import tweepy
import loginSrBot

bot = telebot.TeleBot("")
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_SECRET=""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

SrLogin = loginSrBot.loginSrBot("jasviers7","patata")
Contra = ""

@bot.message_handler(commands=['saludo'])
def hello(message):
	name = message.from_user.username
	bot.reply_to(message, "Buenas " + name)

@bot.message_handler(commands=['tweet'])
def tweet(message):
	print("Antes if")
	if Contra == Contra:
		bot.reply_to(message, "Se tweeteo: " + message.text[7:] )
		api.update_status(message.text[7:])

@bot.message_handler(commands=["contra"])
def contra(message):
	Contra = message.text[8:]
	bot.reply_to(message, "Contrasenia actualizada")
	bot.reply_to(message, message.text[8:])
'''
@bot.message_handler(commands=[""])
def xxx():

@bot.message_handler(commands=[""])
def xxx():

@bot.message_handler(commands=[""])
def xxx():
'''

print("running...")
bot.polling()
