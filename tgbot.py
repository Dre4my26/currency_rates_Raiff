"""
Code for @Raiff_exchange_bot
"""

import telebot
from telebot import types
from exchange_rate import main

TOKEN = input("TOKEN: ")

bot = telebot.TeleBot(TOKEN)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])  # for commands 'start' and 'help'
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start_user_button = types.KeyboardButton("/start")
    price_user_button = types.KeyboardButton("/price")

    markup.add(start_user_button)
    markup.add(price_user_button)

    if message.text == "/start":
        bot.send_message(message.chat.id, "Time to exchange the currency!!",
                         parse_mode="html", reply_markup=markup)


bot.polling(none_stop=True)