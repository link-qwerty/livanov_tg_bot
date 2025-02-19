# Imports
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db.json import JSONHandler

# Code

# create and load data from db
json_db = JSONHandler(config('JSON_FILE'))

# create scheduler
scheduler = AsyncIOScheduler(timezone= 'Europe/Moscow')

# build admins list from .env
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

# configure and create logger
logging.basicConfig(level= logging.INFO, format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# create bot with token from .env and default bot properties
bot = Bot(token= config('TOKEN'), default= DefaultBotProperties(parse_mode= ParseMode.HTML))

# create dispatcher
dispatcher = Dispatcher(storage= MemoryStorage())