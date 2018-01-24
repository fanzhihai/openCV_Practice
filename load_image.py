#coding:utf-8
"""
@auther:BigOceans
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 以灰度模式读入图片
img = cv2.imread('football.jpg',cv2.IMREAD_GRAYSCALE)

# 展示图片
cv2.imshow('image',img)
# 等待键盘键入
cv2.waitKey(0)

# 保存图片
cv2.imwrite('balls',img)

# 删除建立的窗口
cv2.destroyAllWindows()
