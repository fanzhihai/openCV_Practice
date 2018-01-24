#coding=utf-8

import cv2
import numpy as np

# 打开本地视频
capture = cv2.VideoCapture('232.mpg')

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)

    if waitKey(50) & 0xFF == ord('s'):
        break

cv2.realease()
cv2.destroyAllWindows()
