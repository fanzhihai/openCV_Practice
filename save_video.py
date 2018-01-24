#coding=utf-8

import cv2
import numpy as np

# 打开摄像头
capture = cv2.VideoCapture(0)
# 指定FourCC编码
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outVideo.avi',fourcc,15,(680,460))

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        # 垂直翻转图像,1水平翻转，0垂直翻转，-1水平垂直翻转
        frame = cv2.flip(frame,0)
        # 写入视频
        out.write(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
      
capture.release()
out.release()
cv2.destroyAllWindows()

