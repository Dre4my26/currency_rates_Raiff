# -*- coding: utf-8 -*-
"""
Code for @Raiff_exchange_bot
"""

import telebot
from telebot import types
from exchange_rate import main
from tg_checker import extractor, last_rate_saver
from memory_profiler import memory_usage  # для замеров потребления оперативной памяти
import psutil  # для замеров потребления CPU в % (из-за этого бот не отвечает первые 20 секунд после его запуска)

TOKEN = ''

bot = telebot.TeleBot(TOKEN, parse_mode="MARKDOWN")  # You can set parse_mode by default. HTML or MARKDOWN
print("Bot is up and running!")
print(memory_usage())
print('The CPU usage is: ', psutil.cpu_percent(20))


@bot.message_handler(commands=['start', 'help'])  # for command 'start'
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    help_user_button = types.KeyboardButton("/help")
    best_today_user_button = types.KeyboardButton("Лучший курс за сегодня")
    now_user_button = types.KeyboardButton("Курс сейчас")

    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Привет! Теперь я буду оповещать тебя, когда ты можешь переводить валюту из *Райффайзен банка "
                         "в рубли* по лучшему курсу!",
                         reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(now_user_button)
        markup.add(best_today_user_button)
        markup.add(help_user_button)
        print(memory_usage())
        bot.send_message(message.chat.id, 'Выберите, что вам надо', reply_markup=markup)
    if message.text == "/help":
        markup.add(now_user_button)
        markup.add(best_today_user_button)
        bot.send_message(message.chat.id, "Я умею: \n- Присылать курс на данный момент(команда /now)"
                                          "\n- Автоматически присылать лучший курс за день",
                         parse_mode="markdown",
                         reply_markup=markup)


@bot.message_handler(content_types='text')
def now_and_today(message):
    if message.text == "Курс сейчас":
        bot.send_message(message.chat.id, f"Сейчас за 1 евро Вы отдадите {extractor()[0]}руб")
    if message.text == "Лучший курс за сегодня":
        bot.send_message(message.chat.id, f"Лучший курс за сегодня {extractor()[0]} в {extractor()[1].split(' ')[0]}")
        print(memory_usage())


@bot.message_handler(content_types='text')
def send_max_rate():
    if last_rate_saver():
        bot.send_message(863533277, f"Сейчас лучшее время выводить евро! Текущий курс: {extractor()[0]}")


bot.polling(none_stop=True)
