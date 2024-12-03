import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Monumento.jpg')
img_blur = cv2.blur(img, (15,15))
img_median = cv2.medianBlur(img,5)
img_gauss = cv2.GaussianBlur (img, (5,5), 0)
img_bi = cv2.bilateralFilter (img,9,75,75)
img_laplaciano = cv2.Laplacian (img_gauss, cv2.CV_64F)
img_laplaciano_b = img_laplaciano/img_laplaciano.max()





plt.figure(figsize=[5,5])
plt.subplot(321); plt.imshow(img)
plt.subplot(322); plt.imshow(img_blur)
plt.subplot(323); plt.imshow(img_median)
plt.subplot(324); plt.imshow(img_gauss)
plt.subplot(325); plt.imshow(img_bi)
plt.subplot(326); plt.imshow(img_laplaciano_b)
plt.show()