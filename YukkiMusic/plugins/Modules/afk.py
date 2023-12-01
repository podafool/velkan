import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = '5327660504:AAG-G9ZJoyD9Oos_4SxXiA1o7Ibk1GcraIE'
chat_id = None
user_afk = {}

def start(update, context):
    context.bot.send_message(chat_id=chat_id, text='AFK mode enabled!')
    user_afk[update.effective_user.id] = True

def stop(update, context):
    context.bot.send_message(chat_id=chat_id, text='AFK mode disabled!')
    user_afk[update.effective_user.id] = False

def afk_handler(update, context):
    if update.effective_user.id in user_afk:
        return
    user_afk[update.effective_user.id] = True
    context.bot.send_message(chat_id=chat_id, text='User went AFK!')

def unhandled_message(message):
    if message.text == '/afk':
        start(message.update, message.context)
    elif message.text == '/unafk':
        stop(message.update, message.context)
    else:
        return

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(MessageHandler(Filters.text, afk_handler))
    dp.add_handler(MessageHandler(Filters.all, unhandled_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
