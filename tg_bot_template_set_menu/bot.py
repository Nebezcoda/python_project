from aiogram import Bot, Dispatcher
from keyboards.set_menu import set_main_menu
import asyncio
import logging
from aiogram.filters import Command
from aiogram.types import Message
from config_data.config import Config, load_config

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем кнопку Menu
    await set_main_menu(bot)

    # Этот хэндлер будет срабатывать на команду "/delmenu"
    # и удалять кнопку Menu c командами
    @dp.message(Command(commands='delmenu'))
    async def del_main_menu(message: Message, bot: Bot):
        await bot.delete_my_commands()
        await message.answer(text='Кнопка "Menu" удалена')

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())