import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import setting

from emoji import emojize

from glob import glob
from random import randint, choice

logging.basicConfig(filename= "bot1.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = emoji(context.user_data)
    update.message.reply_text(f"Привет, пользователь {context.user_data['emoji']}!")
    
def talk_to_me(update, context):
    context.user_data['emoji'] = emoji(context.user_data) # 1)в emoji отдаем  узердату 3) то что вернул emoji() перезаписываем в юзердата емодзи
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")

def send_cat_pic(update,context):
    cat_pic_list = glob('images/cat*.jpg')
    cat_pic_filename = choice(cat_pic_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))

def emoji(user_data):
    if 'emoji' not in user_data: # 2) идет проверка есть ли смайл или нет 
        smile = choice(setting.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def guess_number(update,context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except(TypeError, ValueError):
            message = "Enter a number"
    else:
        message = "Enter a number"
    update.message.reply_text(message)

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10 , user_number + 10)
    if user_number > bot_number:
        message = f"Your number {user_number}, my number {bot_number}. You are a winner!"
    elif user_number == bot_number:
        message = f"Your number {user_number}, my number {bot_number}. Draw!"
    else:
        message = f"Your number {user_number}, my number {bot_number}. I am a winner!"
    return message


def main():
    mybot = Updater(setting.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_pic))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал!")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
