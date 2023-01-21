import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img_Im = cv2.imread('Yuliy.jpg')
img_Im = cv2.resize(img_Im, (500, 700))
img_I_GRAY = cv2.cvtColor(img_Im, cv2.COLOR_BGR2GRAY)

faces = face_cascades.detectMultiScale(img_I_GRAY)
for (x, y, w, h) in faces:
    cv2.rectangle(img_Im, (x, y), (x + w, y + h), (0, 187, 100), 2)

cv2.imshow('Result', img_Im)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
#     cv2.imshow('camera', frame)

#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break