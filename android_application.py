import cv2
from aiogram.dispatcher.filters import CommandStart
from playsound import playsound
import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio

bot = Bot(token='5678863741:AAHDH5ngAGas2bKIHf7rHHbUaTacoFMdmw8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, text='fdsaf')


if __name__ == '__main__':
    executor.start_polling(dp)