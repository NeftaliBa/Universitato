import cv2
for x in dir(cv2):
    if x.startswith('COLOR_'):
        print(x)


#import cv2
#img = cv2.imread('sample.jpg')
#yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
#cv2.imshow('YUV color space', yuv_img)
#cv2.waitKey()