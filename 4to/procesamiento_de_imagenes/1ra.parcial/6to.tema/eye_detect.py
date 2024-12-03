import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


if face_cascade.empty():
    raise IOError('No se pudo cargar el filtro de cara')
if eye_cascade.empty():
    raise IOError('No se pudo cargar el filtro de ojo')

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
ds_factor = 0.5

while True:
    success, frame = cap.read()
    frame =cv2.flip(frame,1)
    #frame = cv2.resize(frame, None,fx=1, fy=1, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3,5)


    for (x,y,w,h) in faces:
        roi_gray = gray [y: y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(x_eye, y_eye, w_eye, h_eye) in eyes:
            center = (int (x_eye + 0.5 * w_eye), int (y_eye + 0.5 * h_eye))
            radius = int(0.3 * (w_eye + h_eye))
            color = (0,255, 0)
            thickness = 3
            cv2.circle(roi_color, center, radius, color, thickness)
    cv2.imshow('Detector de ojos', frame)
    c = cv2.waitKey(30)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()