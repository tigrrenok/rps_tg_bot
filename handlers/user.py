from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb, game_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner
from services.stats import get_stat, update_stats

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=yes_no_kb)

@router.message(Command(commands="help"))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=yes_no_kb)

@router.message(F.text == LEXICON_RU["yes_button"])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU["yes"], reply_markup=game_kb)

@router.message(F.text == LEXICON_RU["no_button"])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])

@router.message(F.text == LEXICON_RU["get_stat"])
async def process_no_answer(message: Message):
    text = get_stat(message.from_user.id)
    await message.answer(text=text, reply_markup=yes_no_kb)

@router.message(
    F.text.in_([LEXICON_RU["rock"], LEXICON_RU["paper"], LEXICON_RU["scissors"]])
)
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f"{LEXICON_RU['bot_choice']} - {LEXICON_RU[bot_choice]}")
    winner = get_winner(message.text, bot_choice)

    if winner == "user_won":
        message_effect_id = "5046509860389126442"
        update_stats(message.from_user.id, True)
    else:
        message_effect_id = None
        update_stats(message.from_user.id, False)

    await message.answer(
        text=LEXICON_RU[winner],
        message_effect_id=message_effect_id,
        reply_markup=yes_no_kb,
    )

