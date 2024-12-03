import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rec = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_sir = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=[20,5])

plt.subplot(121); plt.imshow(img_rec, cmap="gray")
plt.subplot(122); plt.imshow(img_sir, cmap="gray")

plt.show()


plt.subplot(331); img_bitwise = cv2.bitwise_xor(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "turbo")
plt.subplot(332); img_bitwise = cv2.bitwise_and(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "winter")
plt.subplot(333); img_bitwise = cv2.bitwise_or(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "Reds")
plt.subplot(334); img_bitwise = cv2.bitwise_not(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "turbo")


plt.subplot(335); img_bitwise = cv2.bitwise_xor(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "turbo")
plt.subplot(336); img_bitwise = cv2.bitwise_and(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "winter")
plt.subplot(337); img_bitwise = cv2.bitwise_or(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "Reds")
plt.subplot(338); img_bitwise = cv2.bitwise_not(img_rec,img_sir, mask = None)
plt.imshow(img_bitwise, cmap= "turbo")
plt.show()