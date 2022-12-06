import cv2 as cv

face = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
full_body = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_fullbody.xml')

cap = cv.VideoCapture(0)


while True:
    success, img = cap.read()
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(img_gray, 1.1, 19)
    full_bodys = full_body.detectMultiScale(img_gray, 1.1, 19)

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    #
    for (x,y,w,h) in full_bodys:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 400, 0), 1)


    cv.imshow('detector', img)
    if cv.waitKey(0) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()