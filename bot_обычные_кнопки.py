from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = ''

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# # Создаем объекты кнопок
# button_1 = KeyboardButton(text='Собак 🦮')
# button_2 = KeyboardButton(text='Огурцов 🥒')

# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard = ReplyKeyboardMarkup(
#     keyboard=[[button_1, button_2]],
#     resize_keyboard=True,
#     one_time_keyboard=True
# )

# Пример 1. Создаем клавиатуру из 3-х рядов кнопок по 3 кнопки в каждом ряду.
# # Создаем объекты кнопок
# button_1 = KeyboardButton(text='Кнопка 1')
# button_2 = KeyboardButton(text='Кнопка 2')
# button_3 = KeyboardButton(text='Кнопка 3')
# button_4 = KeyboardButton(text='Кнопка 4')
# button_5 = KeyboardButton(text='Кнопка 5')
# button_6 = KeyboardButton(text='Кнопка 6')
# button_7 = KeyboardButton(text='Кнопка 7')
# button_8 = KeyboardButton(text='Кнопка 8')
# button_9 = KeyboardButton(text='Кнопка 9')

# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard = ReplyKeyboardMarkup(
#     keyboard=[[button_1, button_2, button_3],
#               [button_4, button_5, button_6],
#               [button_7, button_8, button_9]],
#     resize_keyboard=True
# )

# keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
#     text=f'Кнопка {j * 3 + i}') for i in range(1, 4)] for j in range(3)]

# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True
# )

# Пример 2. Клавиатура из 9 кнопок в 5 рядах:
# # Генерируем список с кнопками
# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i}') for i in range(1, 10)]

# # Составляем список списков для будущей клавиатуры
# keyboard: list[list[KeyboardButton]] = [
#     [buttons[0]],
#     buttons[1:3],
#     buttons[3:6],
#     buttons[6:8],
#     [buttons[8]]
# ]

# # Создаем объект клавиатуры, добавляя в него список списков с кнопками
# my_keyboard = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True
# )

# Пример 3. 2 ряда кнопок по 30 кнопок в каждом ряду.
# # Генерируем список с кнопками
# buttons_1: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i}') for i in range(1, 31)]

# # Генерируем список с кнопками
# buttons_2: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i}') for i in range(31, 61)]

# # Составляем список списков для будущей клавиатуры
# keyboard: list[list[KeyboardButton]] = [buttons_1,
#                                         buttons_2]

# # Генерируем список с кнопками
# buttons_1: list[KeyboardButton] = [
#     KeyboardButton(text=f'{i}') for i in range(1, 31)]

# # Генерируем список с кнопками
# buttons_2: list[KeyboardButton] = [
#     KeyboardButton(text=f'{i}') for i in range(31, 61)]

# # Составляем список списков для будущей клавиатуры
# keyboard: list[list[KeyboardButton]] = [buttons_1,
#                                         buttons_2]

# my_keyboard = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True
# )

# Пример 4. Пытаемся сделать 100 рядов по 12 кнопок в каждом.
# buttons: list[KeyboardButton] = []
# keyboard: list[list[KeyboardButton]] = []

# # Заполняем список списками с кнопками
# for i in range(1, 1201):
#     buttons.append(KeyboardButton(text=str(i)))
#     if not i % 12:
#         keyboard.append(buttons)
#         buttons = []

# # Создаем объект клавиатуры, добавляя в него список списков с кнопками
# my_keyboard = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True
# )


# Пример 5. Пытаемся сделать 350 рядов кнопок по одной кнопке в каждом ряду.
# Заполняем список списками с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=f'Кнопка {i}')] for i in range(1, 351)]

# Создаем объект клавиатуры, добавляя в него список списков с кнопками
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки боятся больше?',
        # reply_markup=keyboard
        reply_markup=my_keyboard
    )


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?'
    )


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше'
    )



if __name__ == '__main__':
    dp.run_polling(bot)