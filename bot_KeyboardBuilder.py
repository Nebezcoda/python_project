from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = ''

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Пример 1. Автоматическое размещение 10 кнопок с параметром width=4
# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()

# # Создаем список с кнопками
# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)
# ]

# # Распаковываем список с кнопками в билдер, указываем, что
# # в одном ряду должно быть 4 кнопки
# kb_builder.row(*buttons, width=4)


# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Вот такая получается клавиатура',
#         reply_markup=kb_builder.as_markup(resize_keyboard=True)
#     )

# Пример 2. Автоматическое размещение 8 кнопок с параметром width=3
# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()

# # Создаем список с кнопками
# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i + 1}') for i in range(8)
# ]

# # Распаковываем список с кнопками в билдер, указываем, что
# # в одном ряду должно быть 3 кнопки
# kb_builder.row(*buttons, width=3)


# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Вот такая получается клавиатура',
#         reply_markup=kb_builder.as_markup(resize_keyboard=True)
#     )

# Пример 3. Автоматическое размещение сначала 6-ти кнопок с параметром width=4,
# а затем еще 4-х кнопок с параметром width=3
# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()

# # Создаем первый список с кнопками
# buttons_1: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i + 1}') for i in range(6)
# ]
# # Создаем второй список с кнопками
# buttons_2: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i + 7}') for i in range(4)
# ]
# # Распаковываем список с кнопками в билдер, указываем, что
# # в одном ряду должно быть 4 кнопки
# kb_builder.row(*buttons_1, width=4)

# # Еще раз распаковываем список с кнопками в билдер, указываем, что
# # теперь в одном ряду должно быть 3 кнопки
# kb_builder.row(*buttons_2, width=3)


# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Вот такая получается клавиатура',
#         reply_markup=kb_builder.as_markup(resize_keyboard=True)
#     )

# Пример 4. Создадим клавиатуру, в которую добавим 5 кнопок методом row с параметром width=4,
# а затем добавим еще 10 кнопок методом add.
# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()

# # Создаем первый список с кнопками
# buttons_1: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кн. {i + 1}') for i in range(5)
# ]
# # Создаем второй список с кнопками
# buttons_2: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кн. {i + 6}') for i in range(10)
# ]
# # Распаковываем список с кнопками в билдер методом row,
# # указываем, что в одном ряду должно быть 4 кнопки
# kb_builder.row(*buttons_1, width=4)

# # Распаковываем второй список с кнопками методом add
# kb_builder.add(*buttons_2)


# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Вот такая получается клавиатура',
#         reply_markup=kb_builder.as_markup(resize_keyboard=True)
#     )


# Пример 5. Создадим клавиатуру, добавив 8 кнопок методом add и расставим их так,
# чтобы в 1-м ряду была одна кнопка, во втором - 3, а остальные расставились бы автоматически.
# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()

# # Создаем первый список с кнопками
# buttons_1: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i + 1}') for i in range(8)
# ]
# # Распаковываем список с кнопками методом add
# kb_builder.add(*buttons_1)

# # Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах
# kb_builder.adjust(1, 3)


# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Вот такая получается клавиатура',
#         reply_markup=kb_builder.as_markup(resize_keyboard=True)
#     )

# Пример 6. Создадим клавиатуру с 10 кнопками, переданными в билдер методом add и методом adjust
# разместим их по две в каждом нечетном ряду и по 1 в каждом четном.
# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем первый список с кнопками
buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)
]
# Распаковываем список с кнопками методом add
kb_builder.add(*buttons_1)

# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
kb_builder.adjust(2, 1, repeat=True)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая получается клавиатура',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )



if __name__ == '__main__':
    dp.run_polling(bot)