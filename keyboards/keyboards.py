from aiogram.enums import PollType
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup, KeyboardButtonPollType, WebAppInfo,
)

from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_builder = ReplyKeyboardBuilder()

button_1 = KeyboardButton(text='Помощь')
button_2 = KeyboardButton(text='Поиграем в игру')
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)

poll_quiz_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)
poll_btn = KeyboardButton(
    text='Создать опрос',
    request_poll=KeyboardButtonPollType(type=PollType.REGULAR)
)
quiz_btn = KeyboardButton(
    text='Создать викторину',
    request_poll=KeyboardButtonPollType(type=PollType.QUIZ)
)

web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://stepik.org/")
)

web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True
)

kb_builder.row(button_1, button_2, contact_btn, geo_btn)
kb_builder.row(poll_quiz_btn, poll_btn, quiz_btn,  width=1)

kb_builder.adjust(2, repeat=True)