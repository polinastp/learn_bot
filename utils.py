from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import setting

def main_keyboard():
    return ReplyKeyboardMarkup([['Send a cat', KeyboardButton('My location', request_location=True)]])


def emoji(user_data):
    if 'emoji' not in user_data: # 2) идет проверка есть ли смайл или нет 
        smile = choice(setting.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_numbers(user_number):
    bot_number = randint(user_number - 10 , user_number + 10)
    if user_number > bot_number:
        message = f"Your number {user_number}, my number {bot_number}. You are a winner!"
    elif user_number == bot_number:
        message = f"Your number {user_number}, my number {bot_number}. Draw!"
    else:
        message = f"Your number {user_number}, my number {bot_number}. I am a winner!"
    return message

