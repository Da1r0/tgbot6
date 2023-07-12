from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback.animals import AnimalCallBack

cats = InlineKeyboardButton(text='Котов', callback_data=AnimalCallBack(
    animal='cat',
    count=4
).pack())
dogs = InlineKeyboardButton(text='Собак', callback_data=AnimalCallBack(
    animal='cat',
    count=4
).pack())
cats1 = InlineKeyboardButton(text='Котов2', callback_data=AnimalCallBack(
    animal='cat',
    count=4
).pack())
dogs1 = InlineKeyboardButton(text='Собак2', callback_data=AnimalCallBack(
    animal='cat',
    count=4
).pack())

cats_dogs_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [cats, dogs],
    [cats1, dogs1]
])
