# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: sketch.py
# @Time    : 2021/8/14 11:34
from PIL import Image
import numpy as np
import cv2

def sketch1():
  img = cv2.imread("E:\\ING_19032_02876.jpg")
  # 转换成灰度图片
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # 反转灰度图像
  inverted_image = 255 - gray_img
  # 创建铅笔图
  blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
  inverted_blurred = 255 - blurred
  pencil_sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)
  # 保存
  cv2.imwrite("E:\\ING_19032_02877.jpg",pencil_sketch)
  # 显示
  cv2.imshow("original", img)
  cv2.imshow("pencil", pencil_sketch)
  cv2.waitKey(0)

def sketch2():
    img = np.asarray(Image.open(r"E:\\ING_19032_02876.jpg").convert('L')).astype('float')
    depth = 10.  # (0-100)
    grad = np.gradient(img)  # 取图像灰度的梯度值
    grad_x, grad_y = grad  # 分别取横纵图像梯度值
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A
    vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.  # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
    dz = np.sin(vec_el)  # 光源对z 轴的影响
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    b = b.clip(0, 255)
    im = Image.fromarray(b.astype('uint8'))  # 重构图像
    im.save(r"E:\result111.jpg")
    print("保存成功,请查看")
if __name__ == '__main__':
    sketch1()
    sketch2()