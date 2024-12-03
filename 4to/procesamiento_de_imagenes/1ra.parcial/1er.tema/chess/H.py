import cv2

img = cv2.imread('checkerboard_84x84.jpg')
#               H
cv2.line(img,(0,42),(84,42),(0,0,0),28)

#Mostrar imagen 
cv2.imshow('H',img)
cv2.waitKey(0)
