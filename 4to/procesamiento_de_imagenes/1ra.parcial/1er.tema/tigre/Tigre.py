import cv2

img = cv2.imread('Tigre.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Tigre',img)
cv2.imwrite('Tigre_gris.jpg', img)

print(img.shape)
print(type(img))
print(img.size)
#print(img)

#Mostrar imagen 
cv2.waitKey(0)