from aiogram import F

F.photo                                    # Фильтр для фото
F.voice                                    # Фильтр для голосовых сообщений
F.content_type.in_({ContentType.PHOTO,
                    ContentType.VOICE,
                    ContentType.VIDEO})    # Фильтр на несколько типов контента
F.text == 'привет'                         # Фильтр на полное совпадение текста
F.text.startswith('привет')                # Фильтр на то, что текст сообщения начинается с 'привет'
~F.text.endswith('bot')                    # Инвертирование результата фильтра


# Примеры фильтров через lambda:

lambda message: message.photo                        # Фильтр для фото
lambda message: message.voice                        # Фильтр для голосовых сообщений
lambda message: message.content_type in {ContentType.PHOTO,
                                         ContentType.VOICE,
                                         ContentType.VIDEO}   # Фильтр на несколько типов контента
lambda message: message.text == 'привет'             # Фильтр на полное совпадение текста
lambda message: message.text.startswith('привет')    # Фильтр на то, что текст сообщения начинается с 'привет'
lambda message: not message.text.startswith('bot')   # Инвертирование результата фильтра



# Пример 1. Фильтр, который будет пропускать только апдейты от пользователя с ID = 173901673.

# Через lambda:

lambda message: message.from_user.id == 173901673

# Через F:

F.from_user.id == 173901673

# Пример 2. Фильтр, который будет пропускать только апдейты от админов из списка 193905674, 173901673, 144941561.

# Через lambda:

lambda message: message.from_user.id in {193905674, 173901673, 144941561}

# Через F:

F.from_user.id.in_({193905674, 173901673, 144941561})

# Пример 3. Фильтр, который будет пропускать апдейты текстового типа, кроме тех, которые начинаются со слова "Привет".

# Через lambda:

lambda message: not message.text.startswith('Привет')

# Через F:

~F.text.startswith('Привет')

# Пример 4. Фильтр, который будет пропускать апдейты любого типа, кроме фото, видео, аудио и документов.

# Через lambda:

lambda message: not message.content_type in {ContentType.PHOTO,
                                             ContentType.VIDEO,
                                             ContentType.AUDIO,
                                             ContentType.DOCUMENT}

# Через F:

~F.content_type.in_({ContentType.PHOTO,
                     ContentType.VIDEO,
                     ContentType.AUDIO,
                     ContentType.DOCUMENT})