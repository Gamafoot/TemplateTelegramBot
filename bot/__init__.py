import config
from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

def register_handlers():
    from .handlers import commands
    commands.register_handlers(dp)

def start_bot():
    register_handlers()
    executor.start_polling(dp, skip_updates=True)