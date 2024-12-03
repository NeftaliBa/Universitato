import cv2
import numpy as np
import matplotlib.pyplot as plt

#python3-tk

img = cv2.imread('Tigre.jpg', cv2.IMREAD_UNCHANGED)
img_color = img[:,:,::-1]
img_YCrCB = cv2.cvtColor(img_color, cv2.COLOR_RGB2YCrCb)
img_yuv =cv2.cvtColor(img_color, cv2.COLOR_RGB2YUV)

plt.figure(figsize=[10,5])

plt.subplot(2, 2, 1);plt.imshow(img_color);plt.title("Tigre normal")
plt.subplot(2, 2, 2);plt.imshow(img_YCrCB);plt.title("Tigre en YCRCB")
plt.subplot(2, 2, 4);plt.imshow(img_yuv);plt.title("Tigre en yuv")
plt.subplot(2, 2, 3);plt.imshow(img);plt.title("Tigre en RGB")


plt.show()
