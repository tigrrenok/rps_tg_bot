import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user, other
from keyboards import keyboards

logger = logging.getLogger(__name__)


async def main() -> None:
    """Функция конфигурирования и запуска бота"""

    config: Config = load_config()
    logging.basicConfig(
        level=config.log.level,
        format=config.log.format,
    )
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()
    dp.workflow_data.update({'token': config.bot.token})

    dp.include_router(user.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
