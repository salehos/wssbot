import telebot
import time
from telebot import types


bot_token = '773662304:AAHjQ9orNDCxTQt7wpDT1fo08dKdXgT7qBk'
bot = telebot.TeleBot(bot_token)

user_dict = {}
pm_dict = {}


@bot.message_handler(commands=['start'])
def first_step(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    universityMap = types.KeyboardButton("نقشه دانشگاه")
    tables = types.KeyboardButton("جدول زمان بندی سمینار ها و کارگاه ها")
    introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
    vote = types.KeyboardButton("نظرسنجی")
    contact = types.KeyboardButton("ارتباط با ادمین")
    keyboard.add(universityMap)
    keyboard.add(tables)
    keyboard.add(introduce)
    keyboard.add(vote)
    keyboard.add(contact)
    msg = bot.reply_to(message, 'خوش آمدید. چه کمکی از دست من برمیاد؟', reply_markup=keyboard)
    bot.register_next_step_handler(msg, choosing_one)


def choosing_one(message):
    try:
        if message.text == "نقشه دانشگاه":
            keyboard = types.ReplyKeyboardMarkup()
            keyboard = types.ReplyKeyboardRemove(selective=False)
            photo = open("/home/wssbot/kuroky.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo)
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "جدول زمان بندی سمینار ها و کارگاه ها":
            msg = bot.reply_to(message, "Pre-WSS 2019 Events\n"
                                        "___________________________\n"
                                        "**Dec. 28, 2019**\n"
                                        "16:00 - 19:00\n"
                                        "Alireza Rezaei\n"
                                        "Modeling Diversity in Machine Learning Using Determinantal Point Processes\n"
                                        "**Dec. 29, 2019**\n"
                                        "16:00 - 19:00 \n"
                                        "Behzad Moshiri\n"
                                        "Sensor / Data Fusion, Theoretical and Practical issues\n"
                                        "**Dec. 30, 2019**\n"
                                        "16:00 - 19:00 \n"
                                        "Mohammad Heydari\n"
                                        "Discovering Latent Patterns in Academic Collaboration Network based on Community Detection Approach\n"
                                        "**Dec. 31, 2019**\n"
                                        "16:00 - 19:00 \n"
                                        "Mohammad Khalooei\n"
                                        "Robustness of Deep Neural Networks\n"
                                        "**Jan. 1, 2020**\n"
                                        "16:00 - 19:00 \n"
                                        "Neda Soltani\n"
                                        "Social Network Analysis with Gephi\n"
                                        "**Jan. 1, 2020**\n"
                                        "16:00 - 19:00 \n"
                                        "Mozhgan Mirzaei\n"
                                        "Incidence Theorem and Its Applications\n"
                                        "WSS 2019 Schedule\n"
                                        "___________________________\n"
                                        "TBD\n")
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "آشنایی با ارائه دهنده ها":
            msg = bot.send_message(message.chat.id, "Working...")
            bot.register_next_step_handler(msg, first_step)

        elif message.text == "نظرسنجی":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            seminarvote = types.KeyboardButton("نظرسنجی کلی رویداد")
            speakersvote = types.KeyboardButton("نظرسنجی مربوط به هر سخنرانی")
            keyboard.add(seminarvote)
            keyboard.add(speakersvote)
            msg = bot.reply_to(message, "", reply_markup=keyboard)
            bot.register_next_step_handler(msg, vote_part)
        elif message.text == "ارتباط با ادمین":
            msg = bot.send_message(message.chat.id, "لطفا با @TheMightyM تماس بگیرید")
            bot.register_next_step_handler(msg, choosing_one)
        else:
            raise Exception
    except Exception:
        msg = bot.reply_to(message, "دستور شما جزء دستورات این بات نیست. مجددا تلاش کنید.")
        bot.register_next_step_handler(msg, choosing_one)


def vote_part(message):
    try:
        pass
    except Exception:
        msg = bot.reply_to(message, "What we can do for you?")
        bot.register_next_step_handler(msg, first_step)




def provider(message):
    try



while True:
    try:
        bot.polling()
    except:
        time.sleep(15)

