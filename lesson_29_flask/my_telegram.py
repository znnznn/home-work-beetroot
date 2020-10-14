import logging

import requests
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


news_button = 'Новини сьогодні'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger('my_bot')


def echo_button(update, context: CallbackContext):
    update.message.reply_text(text='news_button', button_echo=ReplyKeyboardRemove())


def echo(update, context: CallbackContext):
    text = update.message.text
    if text == news_button:
        return echo_button(update=update, context=context)
    button_echo = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=news_button), ], ], resize_keyboard=True,)
    update.message.reply_text(text='/start', button_echo=button_echo)


def start(update, context: CallbackContext):
    news_list = requests.get('http://newsapi.org/v2/top-headlines?country=ua&apiKey=77c7b74fb98f4813ac4875e530b4f9e7')
    news = news_list.json()
    t = "\n".join([i['title'] for i in news["articles"]])
    message = f'Новини на сьогодні:\n{t}'

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def caps(update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


if __name__ == '__main__':
    updater = Updater(token='1146907086:AAHJgCyr6hXV1kvf10cTfpG5671AL7bHVB0', use_context=True)
    start_handler = CommandHandler('start', start, filters=Filters.all)
    caps_handler = CommandHandler('caps', caps)
    updater.dispatcher.add_handler(caps_handler)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))
    updater.start_polling()
    updater.idle()