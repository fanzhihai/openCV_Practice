#coding=utf-8

import cv2
import numpy as np

#打开摄像头
capture = cv2.VideoCapture(0)

while True:
    rets, frame = capture.read()
    cv2.imshow('frame',frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    # 按s键退出
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# 释放摄像头
capture.release()
cv2.destroyAllWindows()
