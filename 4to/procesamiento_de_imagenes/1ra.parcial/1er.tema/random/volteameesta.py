import cv2
import numpy as np

img = cv2.imread('ez.jpg')
num_rows, num_cols= img.shape[:2]



img2=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('aytu', img2)

#Mostrar imagen 
cv2.imwrite('ez.jpg', img2)
cv2.waitKey(0)
