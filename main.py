import numpy as np
import cv2

# Классификатор распознавания лиц // Путь, который вы указываете, - это путь к новой папке, которую вы создали
faceCascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

# Определить классификатор глаза
# eyeCascade = cv2.CascadeClassifier(r'E:\cv\face.py\haarcascade_eye.xml')

# Включи камеру
cap = cv2.VideoCapture(1)
ok = True

while ok:
    # Считать изображение в камере, ок - это параметр оценки успешности считывания
    ok, img = cap.read()
    # Преобразовать в изображение в оттенках серого
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Распознавание лиц
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(32, 32)
    )

    # Обнаруживать глаза на основе обнаружения лица
    for (x, y, w, h) in faces:
        fac_gray = gray[y: (y + h), x: (x + w)]
        result = []
        # eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)

        # Преобразование координат глаза, изменение относительного положения в абсолютное положение
        # for (ex, ey, ew, eh) in eyes:
        #     result.append((x + ex, y + ey, ew, eh))

    # Рисуем прямоугольник
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # for (ex, ey, ew, eh) in result:
    #     cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('1', img)

    k = cv2.waitKey(1)
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()

