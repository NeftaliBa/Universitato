import cv2
img = cv2.imread('checkerboard_84x84.jpg')

cv2.imshow('Mi primera imagen', img)
print(img[0,42])
      
cv2.waitKey(0)



