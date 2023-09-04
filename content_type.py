# ContentType.AUDIO == 'audio'                                # True
# ContentType.TEXT == 'text'                                  # True
# ContentType.PHOTO == 'photo'                                # True
# ContentType.STICKER == 'sticker'                            # True
# ContentType.CONTACT == 'contact'                            # True
# ContentType.LOCATION == 'location'                          # True
# ContentType.POLL == 'poll'                                  # True
# ContentType.SUCCESSFUL_PAYMENT == 'successful_payment'      # True
# ContentType.VOICE == 'voice'                                # True
# ContentType.WEB_APP_DATA == 'web_app_data'                  # True

# Пример 1. Хэндлер, обрабатывающий апдейт с типом контента "photo":

# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.content_type == ContentType.PHOTO)
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')

# Равнозначный хэндлер, обрабатывающий апдейт с типом контента "photo":

# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.content_type == 'photo')
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')

# Равнозначный хэндлер, обрабатывающий апдейт с типом контента "photo", в упрощенной записи:

# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.photo)
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')

# Пример 2. Хэндлер, обрабатывающий апдейты с типом контента "voice", "video" и "text":

# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({'voice', 'video', 'text'}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')

# Равнозначный хэндлер, обрабатывающий апдейты с типом контента "voice", "video" и "text":

# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({ContentType.VOICE,
                                ContentType.VIDEO,
                                ContentType.TEXT}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')