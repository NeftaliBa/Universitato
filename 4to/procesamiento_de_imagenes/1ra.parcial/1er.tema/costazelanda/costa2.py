import cv2
import numpy as np
import matplotlib.pyplot as plt

#python3-tk

img = cv2.imread('New_Zealand_Coast.jpg', cv2.IMREAD_UNCHANGED)
img_color = img[:,:,::-1]
img_YCrCB = cv2.cvtColor(img_color, cv2.COLOR_RGB2YCrCb)
img_yuv =cv2.cvtColor(img_color, cv2.COLOR_RGB2YUV)

ksize= (100,100)

matrix1 = np.ones(img_color.shape) * .6
matrix2 = np.ones(img_color.shape) * 1.5
img_oscura = np.uint8(cv2.multiply(np.float64(img_color),matrix1))
img_clara = np.uint16(cv2.multiply(np.float64(img_color),matrix2))

img_borrosa = cv2.blur(img_color, ksize)

plt.figure(figsize=[15,10])

plt.subplot(2, 3, 1);plt.imshow(img_color);plt.title("Costa normal")
plt.subplot(2, 3, 2);plt.imshow(img_borrosa);plt.title("Costa borroso")
plt.subplot(2, 3, 3);plt.imshow(img);plt.title("Costa en RGB")
plt.subplot(2, 3, 4);plt.imshow(img_oscura);plt.title("Costa oscura")
plt.subplot(2, 3, 5);plt.imshow(img_clara);plt.title("Costa clara")



plt.show()
