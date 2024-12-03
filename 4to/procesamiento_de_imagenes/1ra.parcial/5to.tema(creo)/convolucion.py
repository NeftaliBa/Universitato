import cv2
import numpy as np

kernel_enfoque=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
kernel_desenfoque=np.array([[1,1,1],[1,1,1],[1,1,1]])
kernel_realce_de_bordes=np.array([[0,0,0],[-1,1,0],[0,0,0]])
kernel_repujado=np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
kernel_det_borde=np.array([[0,1,0],[1,-4,1],[0,1,0]])
kernel_filtro_sobel=np.array([[-1,0,1],[-2,0,2],[-1,0,0]])
kernel_filtro_sharpen=np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])
kernel_filtro_norte=np.array([[1,1,1],[1,-2,1],[-1,-1,-1]])
kernel_filtro_este=np.array([[-1,1,1],[-1,-2,-1],[-1,1,1]])
kernel_filtro_gauss=np.array([[1,2,3,1,1],[2,7,11,7,2],[3,11,17,11,2],[2,7,11,7,1],[1,2,3,2,1]])

img = cv2.imread('sample.jpg')

img2 = cv2.filter2D(img, -1, kernel_enfoque)

cv2.imshow('imagen original', img)
cv2.imshow('imagen enfoque', img2)

cv2.waitKey