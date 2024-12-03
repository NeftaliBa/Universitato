import cv2
import numpy as np
import matplotlib.pyplot as plt

#python3-tk

img = cv2.imread('New_Zealand_Coast.jpg', cv2.IMREAD_UNCHANGED)
img_color = img[:,:,::-1]
img_YCrCB = cv2.cvtColor(img_color, cv2.COLOR_RGB2YCrCb)
img_yuv =cv2.cvtColor(img_color, cv2.COLOR_RGB2YUV)

ksize= (100,100)
img_borrosa = cv2.blur(img_color, ksize)

plt.figure(figsize=[10,5])

plt.subplot(2, 3, 1);plt.imshow(img_color);plt.title("Costa normal")
plt.subplot(2, 3, 2);plt.imshow(img_borrosa);plt.title("Costa borroso")
plt.subplot(2, 3, 3);plt.imshow(img);plt.title("Costa en RGB")
plt.subplot(2, 3, 4);plt.imshow(img_YCrCB);plt.title("Costa en YCRCB")
plt.subplot(2, 3, 5);plt.imshow(img_yuv);plt.title("Costa en yuv")



plt.show()
