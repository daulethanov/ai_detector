import cv2
from aiogram.dispatcher.filters import CommandStart
from playsound import playsound
import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5678863741:AAHDH5ngAGas2bKIHf7rHHbUaTacoFMdmw8')
dp = Dispatcher(bot)


# chat_id = 'CHAT-ID'



fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


# @dp.message_handler(CommandStart())
# async def botik(message: types.Message):
    # await bot.send_message(message.chat, 'botik')


@dp.message_handler(CommandStart())
async def botiks(message):
    await bot.send_message(message.chat, 'botiks')

while True:
    ret, frame = cap.read()
    # success, img = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(img_gray, 1.1, 19)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
        roi_gray = img_gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        b1 = 'Обноружен огонь'
        # playsound('audio.mp3')

        # botiks()

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        b = 'Найдено лицо'
        # await bot.send_message(msg.from_user.id, b)
        botiks()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



if __name__ == '__main__':
    executor.start_polling(dp)