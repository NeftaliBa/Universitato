import cv2
import numpy as np


img = cv2.imread('Tigre.jpg')
cv2.imshow('Tigre',img)

#              1ra forma de hacerlo
#img2=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow('tigre volteado 90 grados', img2)

num_rows, num_cols= img.shape[:2]
translation_matrix= np.float32([[-1,0,960], [0,1,0]])
print(translation_matrix)

img2=cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('tonito', img2)


#print(img.shape)
#print(type(img))
#print(img.size)
#print(img)

#Mostrar imagen 
cv2.waitKey(0)