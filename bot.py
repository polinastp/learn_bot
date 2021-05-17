import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import setting

logging.basicConfig(filename= "bot1.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, пользователь!")

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("1821534636:AAEKvBxLcLWqcIFumD9wPpfhTFc9Oe5jQsY", use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал!")
    mybot.start_polling()
    mybot.idle()

main()
