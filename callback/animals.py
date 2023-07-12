from aiogram.filters.callback_data import CallbackData

class AnimalCallBack(CallbackData, prefix='animals'):
    animal: str
    count: int
