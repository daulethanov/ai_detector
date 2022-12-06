import cv2
from playsound import playsound
import telebot
import datetime

bot = telebot.TeleBot('5678863741:AAHDH5ngAGas2bKIHf7rHHbUaTacoFMdmw8')
# chat_id = 'CHAT-ID'


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    # success, img = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(img_gray, 1.1, 19)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
        roi_gray = img_gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        b1 = 'Внимание пожар'
        bot.send_message(chat_id=806442044, text=b1)

        playsound('audio.mp3')

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        b = 'Найдено лицо'
        bot.send_message(chat_id=806442044, text=b)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# while True:
#     ret, frame = cap.read()
#     # success, img = cap.read()
#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face.detectMultiScale(img_gray, 1.1, 19)
#
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
#
#     for (x, y, w, h) in fire:
#         cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
#         roi_gray = img_gray[y:y + h, x:x + w]
#         roi_color = frame[y:y + h, x:x + w]
#         b1 = 'Обноружен огонь'
#
#
#         # playsound('audio.mp3')
#         @bot.message_handler(commands=['start'])
#         def start(message):
#             bot.send_message(message.chat.id, b1)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         b = 'Найдено лицо'
#
#
#         @bot.message_handler(commands=['start'])
#         def start(message):
#             bot.send_message(message.chat.id, b)
#
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

bot.polling()