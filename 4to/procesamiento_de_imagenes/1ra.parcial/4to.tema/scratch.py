import cv2
import numpy as np


def detectar_cuadrante(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if x > width/2:
            if y > height/2:
                point_top_left = (int(width/2), int(height/2))
                point_bottom_right = (width-1, height-1)
            else:
                point_top_left = (int(width/2), 0)
                point_bottom_right = (width-1, int(height/2))
        else:
            if y > height/2:
                point_top_left = (0, int(height/2))
                point_bottom_right = (int(width/2), height-1)
            else:
                point_top_left = (0,0)
                point_bottom_right = (int(width/2), int(height/2))
        cv2.rectangle(img, (0,0), (width-1,height-1), (255,255,255), -1)
        cv2.rectangle(img, point_top_left, point_bottom_right, (150,100,150), -1)

if __name__ == '__main__':
    width, height = 640,480
    img = 255 * np.ones((height, width, 3), dtype = np.uint8)
    cv2.namedWindow('Prueba')
    cv2.setMouseCallback('Prueba', detectar_cuadrante)

    while True:
        cv2.imshow('Prueba', img)
        c = cv2.waitKey(10)
        if c == 113 or c == 27 or c == 120:
            break
    cv2.destroyAllWindows()

            
