import cv2
import numpy as np
import matplotlib.pyplot as plt


video = cv2.VideoCapture(0)

if (video.isOpened()== False):
    print("Error al abrir strem de video de la cámara")

while(video.isOpened()):

    ret, frame = video.read()
    ksize= (10,10)

    if ret == True:
        #filtros
        img_borrosa = cv2.blur(frame, ksize)
        cv2.imshow('Mi primero video. con tecla q te sales', img_borrosa)


        #camara gris
        #img = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        #cv2.imshow('Mi primero video. con tecla q te sales', img)


        #matrix2 = np.ones(frame.shape) * 1.5
        #img_clara = np.uint16(cv2.multiply(np.float64(frame),matrix2))
        #cv2.imshow('Mi primero video. con tecla q te sales', img_clara)
        
        
        k= cv2.waitKey(20)
        # tecla 113 es 'q', de 'quit'
        if k == 113:
            break
    else:
        break
video.release()
cv2.destroyAllWindows()

