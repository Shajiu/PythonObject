# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: url_png.py
# @Time    : 2021/10/10 10:54
import qrcode
qr = qrcode.QRCode(
	version=2,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=1
)#设置二维码的大小
qr.add_data("https://shajiu.github.io/")
qr.make(fit=True)
img = qr.make_image()
img.save("./my_blog.png")