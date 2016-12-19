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
api = tweepy.API(auth)

'''
SrLogin = loginSrBot.loginSrBot("jasviers7","patata")
Contra = ""
'''

#Funciones auxiliares

def confirmateUser():
        print('En construccion')

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
                api.update_status(message.text[7:])
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
               user = api.get_user(message.text[10:])
        else:
                bot.reply_to(message, "Ese usuario no existe, compruebe que el nombre esta bien escrito")

@bot.message_handler(commands=['infoMe'])
def infoMe(message):
        user = api.me()
        
@bot.message_handler(commands=['block'])
def block(message):
        if existUser(message.taxt[7:]):
                api.create_block(message.text[7:])
        else:
                bot.reply_to(message,"")



                
                
'''
@bot.message_handler(commands=[""])
def xxx():

@bot.message_handler(commands=[""])
def xxx():
'''

print("running...")
bot.polling()
