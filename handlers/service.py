# Imports
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils.utime import time_of_day_hello
from bot import json_db, admins, dispatcher

# Defines
service_router = Router() # create router for start handlers

@service_router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Функция-обработчик для команды /start

    Декорированная асинхронная функция-фильтр, обрабатывающая команду /start. Открывает диалог с ботом
    :param message: Сообщение от пользователя
    :return: корутина cmd_start()
    """

    await message.answer(json_db.parse('messages', 'start').format(goodday = time_of_day_hello()))

@service_router.message(Command('stop'))
async def cmd_stop(message: Message):
    """
    Функция-обработчик для команды /stop

    Декорированная асинхронная функция-фильтр, обрабатывающая команду /stop. Останавливает опрос бота, после чего
    приложение корректно завершается
    :param message: Сообщение от пользователя
    :return: корутина cmd_stop()
    """

    if message.from_user.id in admins:
        await message.answer(json_db.parse('messages', 'stop'))
        await dispatcher.stop_polling()

@service_router.message(Command('help'))
async def cmd_help(message: Message):
    """
    Функция-обработчик для команды /help

    Декорированная асинхронная функция-фильтр, обрабатывающая команду /help. Останавливает опрос бота, после чего
    приложение корректно завершается
    :param message: Сообщение от пользователя
    :return: корутина cmd_help()
    """

    await message.answer(json_db.parse('messages', 'help'))

@service_router.message(F.text == "Шерлок, покажи что ты можешь")
async def cmd_help_phrase(message: Message):
    """
    Функция-обработчик для фразы Шерлок, покажи что ты можешь

    Декорированная асинхронная функция-фильтр, обрабатывающая сообщение Шерлок, покажи что ты можешь. Выдает
    справку по командам и фразам бота
    :param message: Сообщение от пользователя
    :return: корутина cmd_help_phrase()
    """

    await message.answer(json_db.parse('messages', 'help'))