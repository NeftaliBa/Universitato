import cv2
import numpy as np
import matplotlib.pyplot as plt

#python3-tk

img = cv2.imread('building-windows.jpg', cv2.IMREAD_UNCHANGED)
img_gris = cv2.imread('building-windows.jpg', cv2.IMREAD_GRAYSCALE)
img_color = img[:,:,::-1]

retval, img_tresh = cv2.threshold(img_gris, 100, 255, cv2.THRESH_BINARY)

ksize= (100,100)

matrix1 = np.ones(img_color.shape) * .6
matrix2 = np.ones(img_color.shape) * 1.5
img_oscura = np.uint8(cv2.multiply(np.float64(img_color),matrix1))
img_clara = np.uint16(cv2.multiply(np.float64(img_color),matrix2))

img_borrosa = cv2.blur(img_color, ksize)

plt.figure(figsize=[10,15])

plt.subplot(2, 3, 1);plt.imshow(img_color);plt.title("Edificio normal")
plt.subplot(2, 3, 2);plt.imshow(img_borrosa);plt.title("Edificio borroso")
plt.subplot(2, 3, 3);plt.imshow(img_oscura);plt.title("Edificio oscura")
plt.subplot(2, 3, 4);plt.imshow(img_clara);plt.title("Edificio clara")
plt.subplot(2, 3, 5);plt.imshow(img_gris, cmap="gray");plt.title("Edificio gris")
plt.subplot(2, 3, 6);plt.imshow(img_clara, cmap="gray");plt.title("Edificio con umbral")



plt.show()