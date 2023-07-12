import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from callback.animals import AnimalCallBack
from config import config
from keyboards.inline import cats_dogs_keyboards


API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def start_command(message: Message):
    await message.answer('Привет. Ты любишь котов или собак?', reply_markup=cats_dogs_keyboards)

@dp.callback_query(AnimalCallBack.filter())
async def handle_cats(query: CallbackQuery, callback_data: AnimalCallBack):
    await query.answer(f'Вы нажали кнопку')


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

