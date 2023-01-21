# import cv2 # подключение библиотеки 

# img = cv2.imread('Yuliy.jpg')# задаём переменную. cv2 - оюращаемся к библиотеке. imread('BMW.jpg') - вызываем метод и в скобках 
                        # указываем название картинки, если она есть в папке вместе с файлом программы. Если нет, то вместа
                        # пишим путь к картинике.
# print(img.shape) #выведет в консоль размер картинки и цифра 3 говорит, что на каждый пиксель 3 канала: красный, зелёный и синий
# img = cv2.resize(img, (500, 700)) #эта команда изменит размер картинки в пикселях.

# cv2.imshow('Result', img) # эта команда покажет картинку на экране. Result - так мы называем окошко, в котором будет картинка.
                            # всё выполнится, но окошко сразу же закроется. Нужно поставитть ожидание. Это следующая команда.

# cv2.waitKey(0) # Ноль означает, что картинка не закроется, пока сам не закрою, если указать, например 1000, то картинка закроется
                # через 1000 миллисекунд

# ---------Ниже: определяет на картинке есть ли лицо
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