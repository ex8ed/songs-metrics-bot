from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# keyboards for each step of creating stata:
mood_chooser = InlineKeyboardMarkup(row_width=2)
zodiac_chooser = InlineKeyboardMarkup(row_width=2)
event_chooser = InlineKeyboardMarkup(row_width=2)
fos_chooser = InlineKeyboardMarkup(row_width=2)
age_chooser = InlineKeyboardMarkup(row_width=2)
clip_chooser = InlineKeyboardMarkup(row_width=2)
men_chooser = InlineKeyboardMarkup(row_width=2)

# mood chooser buttons:
btn_mood_drive = InlineKeyboardButton(text='Драйвовое', callback_data='btn_mood_drive')
btn_mood_melancholy = InlineKeyboardButton(text='Меланхоличное', callback_data='btn_mood_melancholy')
btn_mood_freedom = InlineKeyboardButton(text='Свобода', callback_data='btn_mood_freedom')
btn_mood_hurt = InlineKeyboardButton(text='Обида', callback_data='btn_mood_hurt')
btn_mood_sure = InlineKeyboardButton(text='Уверенное', callback_data='btn_mood_sure')
btn_mood_passionate = InlineKeyboardButton(text='Страстное', callback_data='btn_mood_passionate')

# zodiac chooser buttons:
btn_zodiac_aquarius = InlineKeyboardButton(text='Водолей', callback_data='btn_zodiac_aquarius')
btn_zodiac_pisces = InlineKeyboardButton(text='Рыбы', callback_data='btn_zodiac_pisces')
btn_zodiac_aries = InlineKeyboardButton(text='Овен', callback_data='btn_zodiac_aries')
btn_zodiac_taurus = InlineKeyboardButton(text='Телец', callback_data='btn_zodiac_taurus')
btn_zodiac_gemini = InlineKeyboardButton(text='Близнецы', callback_data='btn_zodiac_gemini')
btn_zodiac_cancer = InlineKeyboardButton(text='Рак', callback_data='btn_zodiac_cancer')
btn_zodiac_leo = InlineKeyboardButton(text='Лев', callback_data='btn_zodiac_leo')
btn_zodiac_virgo = InlineKeyboardButton(text='Дева', callback_data='btn_zodiac_virgo')
btn_zodiac_libra = InlineKeyboardButton(text='Весы', callback_data='btn_zodiac_libra')
btn_zodiac_scorpio = InlineKeyboardButton(text='Скорпион', callback_data='btn_zodiac_scorpio')
btn_zodiac_sagittarius = InlineKeyboardButton(text='Стрелец', callback_data='btn_zodiac_sagittarius')
btn_zodiac_capricorn = InlineKeyboardButton(text='Козерог', callback_data='btn_zodiac_capricorn')

# event chooser buttons
btn_event_date = InlineKeyboardButton(text='Свидание', callback_data='btn_event_date')
btn_event_car = InlineKeyboardButton(text='Машина', callback_data='btn_event_car')
btn_event_exams = InlineKeyboardButton(text='Сессия', callback_data='btn_event_exams')
btn_event_breaking_up = InlineKeyboardButton(text='Расставание', callback_data='btn_event_breaking_up')
btn_event_nostalgia = InlineKeyboardButton(text='Ностальгия', callback_data='btn_event_nostalgia')
btn_event_being_in_love = InlineKeyboardButton(text='Влюбленность', callback_data='btn_event_being_in_love')
btn_event_flirt = InlineKeyboardButton(text='Флирт', callback_data='btn_event_flirt')

# feat or single buttons
btn_fos_feat = InlineKeyboardButton(text='Feat', callback_data='btn_fos_feat')
btn_fos_single = InlineKeyboardButton(text='Single', callback_data='btn_fos_single')

# age chooser buttons
btn_age_old = InlineKeyboardButton(text='Лучше старый Егор Крид', callback_data='btn_age_old')
btn_age_new = InlineKeyboardButton(text='Лучше новый Егор Крид', callback_data='btn_age_new')

# clip chooser buttons
btn_clip_yes = InlineKeyboardButton(text='Да, клип нужен', callback_data='btn_clip_yes')
btn_clip_no = InlineKeyboardButton(text='Нет, клип до лампочки', callback_data='btn_clip_no')

# men chooser buttons
btn_men_romantic = InlineKeyboardButton(text='Романтичный', callback_data='btn_men_romantic')
btn_men_persistent = InlineKeyboardButton(text='Настойчивый', callback_data='btn_men_persistent')
btn_men_energy = InlineKeyboardButton(text='Заряженный', callback_data='btn_men_energy')
btn_men_muscle = InlineKeyboardButton(text='Маскулинный', callback_data='btn_men_muscle')

mood_chooser.insert(btn_mood_drive)
mood_chooser.insert(btn_mood_melancholy)
mood_chooser.insert(btn_mood_freedom)
mood_chooser.insert(btn_mood_hurt)
mood_chooser.insert(btn_mood_sure)
mood_chooser.insert(btn_mood_passionate)

zodiac_chooser.insert(btn_zodiac_aquarius)
zodiac_chooser.insert(btn_zodiac_pisces)
zodiac_chooser.insert(btn_zodiac_aries)
zodiac_chooser.insert(btn_zodiac_taurus)
zodiac_chooser.insert(btn_zodiac_gemini)
zodiac_chooser.insert(btn_zodiac_cancer)
zodiac_chooser.insert(btn_zodiac_leo)
zodiac_chooser.insert(btn_zodiac_virgo)
zodiac_chooser.insert(btn_zodiac_libra)
zodiac_chooser.insert(btn_zodiac_scorpio)
zodiac_chooser.insert(btn_zodiac_sagittarius)
zodiac_chooser.insert(btn_zodiac_capricorn)

event_chooser.insert(btn_event_date)
event_chooser.insert(btn_event_car)
event_chooser.insert(btn_event_exams)
event_chooser.insert(btn_event_breaking_up)
event_chooser.insert(btn_event_nostalgia)
event_chooser.insert(btn_event_being_in_love)
event_chooser.insert(btn_event_flirt)

fos_chooser.insert(btn_fos_feat)
fos_chooser.insert(btn_fos_single)

age_chooser.insert(btn_age_old)
age_chooser.insert(btn_age_new)

clip_chooser.insert(btn_clip_no)
clip_chooser.insert(btn_clip_yes)

men_chooser.insert(btn_men_romantic)
men_chooser.insert(btn_men_persistent)
men_chooser.insert(btn_men_energy)
men_chooser.insert(btn_men_muscle)
