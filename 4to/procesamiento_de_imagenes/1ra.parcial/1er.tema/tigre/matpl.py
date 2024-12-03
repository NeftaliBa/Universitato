import cv2
import numpy as np
import matplotlib.pyplot as plt

#python3-tk

img = cv2.imread('Tigre.jpg', cv2.IMREAD_COLOR)
#cv2.imshow('Tigre',img)

img_color = img[:,:,::-1]
img_yuv = cv2.cvtColor(img_color, cv2.COLOR_RGB2YCR_CB)
plt.imshow(img_yuv)
plt.title("tigre")
plt.show()



