import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# reading the image using imread
img = cv2.imread('images.jpg')
# converting coloured image into grayscale for identification
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1 ,4)
# dimension of recognition box
for (x, y , w , h) in faces:
    cv2.rectangle(img, (x , y ),(x+w , y+h),(255, 0, 0) , 2)
    # displaying the image
cv2.imshow('img', img)
cv2.waitKey()
