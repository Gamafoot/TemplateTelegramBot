from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext

async def start(msg: types.Message, state:FSMContext):
    await msg.answer('Добро пожаловать в бота!')