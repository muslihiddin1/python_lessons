from transliterator import to_cyrillic, to_latin
import telebot

TOKEN = "8311142197:AAHpKF5u0BM4zFaI02UehCIcDemBq2Zur90"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    matn = message.text
    javob = lambda matn: to_cyrillic(matn) if matn.isascii() else to_latin(matn)
    # if matn.isascii():
    #     javob = to_cyrillic(matn)
    # else:
    #     javob = to_latin(matn)
    bot.reply_to(message, javob(matn))

bot.polling()


# matn = input("Matn kiriting: ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))