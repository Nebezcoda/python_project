from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)