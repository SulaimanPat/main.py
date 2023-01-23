from aiogram import Dispatcher, Bot
from decouple import config

TOKEN = config("TOKEN")
ADMINS=(576190634, )


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)