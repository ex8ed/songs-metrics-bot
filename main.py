# -*- coding: UTF-8 -*-
from logging import basicConfig, INFO
import os
import config
import markups
from aiogram import Bot, executor, types, Dispatcher

API_TOKEN = os.getenv("bot-api-token")
# parameters for calculate results
params = {}

# Basic parameters
basicConfig(level=INFO)
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


# main algorythm
def generate_playlist(params: dict):
    accept = []
    for key in config.metrics.keys():
        n = 0
        if config.metrics[key][0] == params['MOOD']:
            n += 1
        if config.metrics[key][1] == params['ZODIAC']:
            n += 1
        if config.metrics[key][2] == params['EVENT']:
            n += 1
        if config.metrics[key][3] == params['FOS']:
            n += 1
        if config.metrics[key][4] == params['AGE']:
            n += 1
        if config.metrics[key][5] == params['CLIP']:
            n += 1
        if config.metrics[key][6] == params['MEN']:
            n += 1
        if n >= 4:
            accept.append(key)
    if len(accept) == 0:
        return 'К сожалению подходящих песен не нашлось. Будьте счастливы с целой психикой. Введите /start для повтора.'
    else:
        return f'Да простит Господь, советую вам послушать: {", ".join(accept)}'


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, config.start_message, reply_markup=markups.mood_chooser)


# returning mood status callbacks:
@dp.callback_query_handler(text='btn_mood_drive')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MOOD"] = 'драйвовое'
    await bot.send_message(message.from_user.id, config.zodiac_step_message, reply_markup=markups.zodiac_chooser)


@dp.callback_query_handler(text='btn_mood_melancholy')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MOOD"] = 'меланхоличное'
    await bot.send_message(message.from_user.id, config.zodiac_step_message, reply_markup=markups.zodiac_chooser)


@dp.callback_query_handler(text='btn_mood_freedom')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MOOD"] = 'свобода'
    await bot.send_message(message.from_user.id, config.zodiac_step_message, reply_markup=markups.zodiac_chooser)


@dp.callback_query_handler(text='btn_mood_hurt')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MOOD"] = 'обида'
    await bot.send_message(message.from_user.id, config.zodiac_step_message, reply_markup=markups.zodiac_chooser)


@dp.callback_query_handler(text='btn_mood_sure')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MOOD"] = 'уверенное'
    await bot.send_message(message.from_user.id, config.zodiac_step_message, reply_markup=markups.zodiac_chooser)


@dp.callback_query_handler(text='btn_mood_passionate')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MOOD"] = 'страстное'
    await bot.send_message(message.from_user.id, config.zodiac_step_message, reply_markup=markups.zodiac_chooser)


# returning zodiac
@dp.callback_query_handler(text='btn_zodiac_aquarius')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'водолей'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_pisces')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'рыбы'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_taurus')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'телец'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_gemini')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'близнецы'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_cancer')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'рак'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_leo')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'лев'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_virgo')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'дева'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_libra')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'весы'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_scorpio')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'скорпион'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_sagittarius')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'стрелец'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


@dp.callback_query_handler(text='btn_zodiac_capricorn')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["ZODIAC"] = 'козерог'
    await bot.send_message(message.from_user.id, config.event_step_message, reply_markup=markups.event_chooser)


# returning an actual event
@dp.callback_query_handler(text='btn_event_date')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'свидание'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


@dp.callback_query_handler(text='btn_event_car')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'машина'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


@dp.callback_query_handler(text='btn_event_exams')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'сессия'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


@dp.callback_query_handler(text='btn_event_breaking_up')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'расставание'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


@dp.callback_query_handler(text='btn_event_nostalgia')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'ностальгия'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


@dp.callback_query_handler(text='btn_event_being_in_love')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'влюбленность'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


@dp.callback_query_handler(text='btn_event_flirt')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["EVENT"] = 'флирт'
    await bot.send_message(message.from_user.id, config.fos_step_message, reply_markup=markups.fos_chooser)


# feat or single info
@dp.callback_query_handler(text='btn_fos_feat')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["FOS"] = 'feat'
    await bot.send_message(message.from_user.id, config.age_step_message, reply_markup=markups.age_chooser)


@dp.callback_query_handler(text='btn_fos_single')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["FOS"] = 'single'
    await bot.send_message(message.from_user.id, config.age_step_message, reply_markup=markups.age_chooser)


# Egor Krid age status:
@dp.callback_query_handler(text='btn_age_old')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["AGE"] = 'старый'
    await bot.send_message(message.from_user.id, config.clip_step_message, reply_markup=markups.clip_chooser)


@dp.callback_query_handler(text='btn_age_new')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["AGE"] = 'новый'
    await bot.send_message(message.from_user.id, config.clip_step_message, reply_markup=markups.clip_chooser)


# clip choose status:
@dp.callback_query_handler(text='btn_clip_yes')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["CLIP"] = 'да'
    await bot.send_message(message.from_user.id, config.men_step_message, reply_markup=markups.men_chooser)


@dp.callback_query_handler(text='btn_clip_no')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["CLIP"] = 'нет'
    await bot.send_message(message.from_user.id, config.men_step_message, reply_markup=markups.men_chooser)


# men choose status:
@dp.callback_query_handler(text='btn_men_romantic')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MEN"] = 'романтичный'
    await bot.send_message(message.from_user.id, generate_playlist(params))


@dp.callback_query_handler(text='btn_men_persistent')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MEN"] = 'настойчивый'
    await bot.send_message(message.from_user.id, generate_playlist(params))


@dp.callback_query_handler(text='btn_men_energy')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MEN"] = 'заряженный'
    await bot.send_message(message.from_user.id, generate_playlist(params))


@dp.callback_query_handler(text='btn_men_muscle')
async def get_mood_drive(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    params["MEN"] = 'маскулинный'
    await bot.send_message(message.from_user.id, generate_playlist(params))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
