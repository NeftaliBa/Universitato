import cv2
import numpy as np


def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing, top_left_pt, bottom_right_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            top_left_pt = (min(x_init, x), min(y_init, y))
            bottom_right_pt = (max(x_init, x), max(y_init, y))
            img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt = (min(x_init, x), min(y_init, y))
        botttom_right_pt = (max(x_init, x), max(y_init, y))
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]


if __name__ == '__main__':
    drawing = False
    top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Jaja que tonto no sabe programar xD")
    cv2.namedWindow('Ventana')
    cv2.setMouseCallback('Ventana', draw_rectangle)

    while True:
        ret, frame = cap.read()


        #blush
        ksize= (10,10)
        blush = cv2.blur(frame, ksize)
        efects = blush

        img = cv2.resize(frame, None, fx=1, fy=1,
                         interpolation=cv2.INTER_AREA)
        (x0, y0), (x1, y1) = top_left_pt, bottom_right_pt
        img[y0:y1, x0:x1] = 255 - efects[y0:y1, x0:x1]
        cv2.imshow('Ventana', img)

        c = cv2.waitKey(1)
        if c == 113 or c == 27 or c == 120:
            break

cap.release()
cv2.destroyAllWindows()
