import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import setting

from handlers import greet_user, user_location, send_cat_pic, guess_number, talk_to_me

logging.basicConfig(filename= "bot1.log", level=logging.INFO)


def main():
    mybot = Updater(setting.API_KEY, use_context=True) # most common handlers should be located in the end
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_pic))
    dp.add_handler(MessageHandler(Filters.regex('^(Send a cat)$'), send_cat_pic)) # та фраза на которую бот должен реагировать (кнопки)
    dp.add_handler(MessageHandler(Filters.location, user_location))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал!")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
