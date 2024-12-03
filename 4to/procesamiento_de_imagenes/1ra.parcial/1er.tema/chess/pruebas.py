import cv2

img = cv2.imread('Tigre.jpg')

#                               Esto lo use de prueba
#   drawMarker(img, (x  , y),   color  ,     tipo de forma   , ancho, ancho de linea)
#cv2.drawMarker(img, (14, 42), (0, 0, 0), cv2.MARKER_SQUARE, 28, 1)
#cv2.drawMarker(img, (70, 42), (0 ,0 ,0), cv2.MARKER_SQUARE, 28, 1)

#               H
#cv2.line(img,(0,42),(84,42),(0,0,0),28)

#               I
#cv2.line(img,(0,14),(84,14),(0,0,0),28)
#cv2.line(img,(0,70),(84,70),(0,0,0),28)

#           Metodo de gaona
#cv2.rectangle ( (img),(0,28),(28,56),(0,0,0),-1)
#cv2.rectangle ( (img),(55,28),(84,56),(0,0,0),-1)

print(img.shape)
print(type(img))
print(img.size)
#print(img)

#Mostrar imagen 
cv2.imshow('Tigre',img)
cv2.waitKey(0)