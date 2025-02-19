# Imports
import asyncio
from bot import scheduler, bot, dispatcher
from handlers.service import service_router

# Defines
async def main():
    """
    Точка входа в приложение

    Асинхронная главная функция - точка входа в приложение. Привязывает к диспетчеру роутеры из пакетов хендлеров,
    инициализирует прочие бизнес-функции. Запускает опрос бота
    :return: корутина main()
    """

    dispatcher.include_router(service_router)
    await bot.delete_webhook(drop_pending_updates= True)
    await dispatcher.start_polling(bot)

#Code
if __name__ == '__main__':
    asyncio.run(main())