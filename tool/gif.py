# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: gif.py
# @Time    : 2021/8/19 08:18

import os
from PIL import Image

'''
1. 获取需要生成 GIF 的图片。
2. 获取第一张图片（这里我选择第一张图片作为 GIF 的首图）。
3. 遍历图片，将图片添加到 images 对象存储。
4. 生成动图。这里有几个参数，其中 loop 表示循环次数，duration 表示图片播放间隔，单位是毫秒。
'''
def generate_gif():
    imgFolderPath = "G:\图片\\17张程序员专属壁纸（后续将持续更新）"
    fileList = os.listdir(imgFolderPath)
    firstImgPath = os.path.join(imgFolderPath, fileList[0])
    im = Image.open(firstImgPath)
    images = []
    for img in fileList[1:]:
        imgPath = os.path.join(imgFolderPath, img)
        images.append(Image.open(imgPath))
    im.save('E:\\result.gif', save_all=True, append_images=images, loop=0, duration=500)

if __name__ == '__main__':
    generate_gif()


