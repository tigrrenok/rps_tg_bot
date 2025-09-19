from aiogram import Router, F
from aiogram.enums import PollType
from aiogram.types import Message, PollAnswer, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.set_menu import kb_builder, web_app_keyboard

# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=kb_builder.as_markup(resize_keyboard=True))


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# Этот хэндлер будет срабатывать на отправку контакта
@router.message(F.contact)
async def process_contact(message: Message):
    await message.answer(
        text=f'Ваш телефон: {message.contact.phone_number}',
    )


# Этот хэндлер будет срабатывать на отправку локации
@router.message(F.location)
async def process_location(message: Message):
    await message.answer(
        text=f'Ваши координаты: {message.location.latitude, message.location.longitude}',
    )

@router.message(F.poll.type == PollType.QUIZ)
async def process_poll_quiz(message: Message):
    await message.answer_poll(
        question=message.poll.question,
        options=[opt.text for opt in message.poll.options],
        is_anonymous=False,
        type=message.poll.type,
        correct_option_id=message.poll.correct_option_id,
        explanationf=message.poll.explanation,
        explanation_entities=message.poll.explanation_entities,
        message_effect_id='5104841245755180586'
    )


# Этот хэндлер будет срабатывать на отправку опроса
@router.message(F.poll.type == PollType.REGULAR)
async def process_poll_reqular(message: Message):
    await message.answer_poll(
        question=message.poll.question,
        options=[opt.text for opt in message.poll.options],
        is_anonymous=False,
        type=message.poll.type,
        allows_multiple_answers=message.poll.allows_multiple_answers,
        message_effect_id='5107584321108051014'
    )


# Этот хэндлер будет срабатывать на отправку опроса ответа в опросе/викторине
@router.poll_answer()
async def process_answer_poll(poll_answer: PollAnswer):
    print(poll_answer.model_dump_json(indent=4, exclude_none=True))

@router.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=web_app_keyboard
    )

# Этот хэндлер будет срабатывать на кнопку 'Поиграем в игру'
@router.message(F.text == 'Поиграем в игру')
async def process_dog_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['game'],
        reply_markup=ReplyKeyboardRemove()
    )


# Этот хэндлер будет срабатывать на остальные сообщения эхом,
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])