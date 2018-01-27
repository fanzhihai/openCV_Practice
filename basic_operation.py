# -*- coding:utf-8 -*-

import cv2
import numpy as np


# 获取并修改像素值
img = cv2.imread('football.jpg')
# 获取像素值
print(img.item(10,10,2))
# 修改像素值为100
img.itemset((10,10,2),100)
# 打印像素值
print(img.item(10,10,2))

# 获取图像形状，返回值包括行数、列数、通道数的元组
print(img.shape)

# 返回图像的像素数目
print(img.size)

# 返回图像的数据类型
print(img.dtype)

# 图像ROI，将部分图像拷贝到其他地方
# ball = img[100:700,100:500]
# img[100:700,500:900] = ball
# cv2.imshow('image',img)

# 拆分和合并图像通道
# r, g, b = cv2.split(img)
# img = cv2.merge(r,g,b)

# 为图像扩边
import matplotlib.pyplot as plt


# cv2.BORDER_REPLICATE复后一个元素
replicate = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REPLICATE)
# cv2.BORDER_REFLECT边界元素的滤镜
reflect = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT)
# cv2.BORDER_REFLECT101边界元素的滤镜,跟上面的类似，但稍有改动
reflect101 = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT101)
# cv2.BORDER_WRAP
wrap = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_WRAP)
# cv2.BORDER_CONSTANT添加有颜色的常数值边界
blue = [255,0,0]
constant = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=blue)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')

plt.show()
