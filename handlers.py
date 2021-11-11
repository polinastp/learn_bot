from glob import glob
from random import randint, choice

from utils import emoji, play_random_numbers, main_keyboard

def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = emoji(context.user_data)
    update.message.reply_text(
        f"Привет, пользователь {context.user_data['emoji']}!",
        reply_markup = main_keyboard()
    )
    

def talk_to_me(update, context):
    context.user_data['emoji'] = emoji(context.user_data) # 1)в emoji отдаем  узердату 3) то что вернул emoji() перезаписываем в юзердата емодзи
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup = main_keyboard())


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
    update.message.reply_text(message, reply_markup = main_keyboard())


def user_location(update, context):
    context.user_data['emoji'] = emoji(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Your coordinates {coords} {context.user_data['emoji']}",
        reply_markup=main_keyboard()
    )
    print(coords)


def send_cat_pic(update,context):
    cat_pic_list = glob('images/cat*.jpg')
    cat_pic_filename = choice(cat_pic_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'), reply_markup = main_keyboard())

