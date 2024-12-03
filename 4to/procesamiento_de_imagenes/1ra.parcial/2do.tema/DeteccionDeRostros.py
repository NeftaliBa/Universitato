import cv2
def detect (filename):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale (gray, 1.3,1)
    for(x,y,w,h) in faces:
        img=cv2.rectangle (img, (x,y), (x+w,y+h), (255,0,0), 2)
    cv2.namedWindow('Rostros detectados!!')
    cv2.imshow('Rostros detectados!!', img)
#   cv2.imwrite('image.jpg', img)
    cv2.waitKey(0)

detect('grupo.jpg')

