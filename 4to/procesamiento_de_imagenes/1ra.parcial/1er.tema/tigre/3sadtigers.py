import cv2
import numpy as np

img = cv2.imread('Tigre.jpg')
cv2.imshow('Tigre',img)

num_rows, num_cols= img.shape[:2]
#rotacion
rotation_matrix= cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 45,1)
img2= cv2.warpAffine(img, rotation_matrix, (num_cols,num_rows))
#traslacion
translation_matrix= np.float32([[-1,0,960], [0,1,0]])
img3=cv2.warpAffine(img2, translation_matrix, (num_cols, num_rows))

print(translation_matrix)
#redimensionar
img4=cv2.resize(img3, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)


#Mostrar imagen 
cv2.imshow('tonito', img4)
cv2.imwrite('3_tristes_tigres.jpg', img4)




cv2.waitKey(0)