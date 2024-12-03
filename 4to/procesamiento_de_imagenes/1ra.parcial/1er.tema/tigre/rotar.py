import cv2
import numpy as np


img = cv2.imread('Tigre.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Tigre',img)

#              1ra forma de hacerlo
#img2=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow('tigre volteado 90 grados', img2)

num_rows, num_cols= img.shape[:2]
rotation_matrix= cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 45,1)
img2= cv2.warpAffine(img, rotation_matrix, (num_cols,num_rows))
cv2.imshow('tigre volteado 45 grados', img2)


#print(img.shape)
#print(type(img))
#print(img.size)
#print(img)

#Mostrar imagen 
cv2.waitKey(0)