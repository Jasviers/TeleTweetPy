# @Author: Javier Antonio Román López (SrGatito)
# @Email: jasviers@gmail.com
# @Version: alpha 2.0.1

import telebot
import tweepy
import loginSrBot

#Creacion de objetos necesarios
bot = telebot.TeleBot("")
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_SECRET=""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
twitter = tweepy.API(auth)

'''
SrLogin = loginSrBot.loginSrBot("jasviers7","patata")
Contra = ""
'''

#Funciones auxiliares

def confirmateUser():
        return True

def existUser(text):
        try:
                api.get_user(text)
                return True
        except TweepError:
                return False

#Cada uno de los comandos para telegram

@bot.message_handler(commands=['pin'])
def hello(message):
	bot.reply_to(message, "pon")

@bot.message_handler(commands=['tweet'])
def tweet(message):
        if len(message.text)< 147:
                twitter.update_status(message.text[7:])
                bot.reply_to(message, "Tweet publicado")
        else:
                bot.reply_to(message, "El tweet es demasiado largo, el maximo son 140 caracteres")
                bot.reply_to(message, "Usaste:  "+(len(message.text)-7) +" caracteres")

'''        
@bot.message_handler(commands=["contra"])
def contra(message):
	Contra = message.text[8:]
	bot.reply_to(message, "Contrasenia actualizada")
	bot.reply_to(message, message.text[8:])
'''

# No testeados o trabajando en ellos
@bot.message_handler(commands=['infoUser'])
def infoUser(message):
        if existUser(message.text[10:]):
                user = twitter.get_user(message.text[10:])
        else:
                bot.reply_to(message, "Ese usuario no existe, compruebe que el nombre esta bien escrito")

@bot.message_handler(commands=['infoMe'])
def infoMe(message):
        user = twitter.me()
        
@bot.message_handler(commands=['block'])
def block(message):
        if existUser(message.text[7:]) and confirmateUser():
                twitter.create_block(message.text[7:])
        else:
                bot.reply_to(message,"")

@bot.message_handler(commands=['tl'])
def timeline(message):
	if confirmateUser():
		tl = twitter.home_timeline()
		for tweet in tl: 
			bot.reply_to(message, )

@bot.message_handler(commands=['delete'])
def delete(message):
	if confirmateUser():
		tl = twitter.home_timeline()
		n = 0
		encontrado = True #Cambiar el nombre
		while encontrado: #Investigar porque hice este tipo de cagada tan horrible
			if api.me() == tl[n].user.id:
				api.destroy_status(tl[n].id)
				bot.reply_to(message, "The last tweet is delete")
				encontrado = False

@bot.message_handler(commands=['block'])
def block(message):
        if existUser(message.text[7:]) and confirmateUser() :
                twitter.create_block(message.text[7:])
                bot.reply:to(message, "Se bloqueo de forma correcta.")
        else:
                bot.reply_to(message, "No se pudo bloquear.")

@bot.message_handler(commands=['unblock'])
def unblock(message):
        if existUser(message.text[9:]) and confirmateUser() :
                twitter.destroy_block(message.text[9:])
                bot.reply:to(message, "Se desbloqueo de forma correcta.")
        else:
                bot.reply_to(message, "No se pudo desbloquear.")
                
'''
@bot.message_handler(commands=[""])
def xxx():

@bot.message_handler(commands=[""])
def xxx():
'''

print("running...")
bot.polling()
