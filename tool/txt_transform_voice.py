# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: txt_transform_voice.py
# @Time    : 2021/10/8 20:30
import pdfplumber
import pyttsx3

'''
功能: 文本转语音
https://mp.weixin.qq.com/s/Z5wLbJ9v6beSVDtYp9oPVA
'''
def read_pdf(file):
    '''
    pdf转text
    :param file:传入待转换为pdf
    :return:  转换后的文本
    '''
    with pdfplumber.open(file) as pdf:
        page=pdf.pages[3]
        text=page.extract_text()
        print("转换的文本文件:",text)
        read_by_mp3(text)

def read_by_mp3(text):
    '''
    文本转语音
    :param text: 文本内容
    :return:     转换后的语音
    '''
    engine=pyttsx3.init()
    text=text.replace("\n","")
    engine.say(text)
    engine.runAndWait()
    engine.save_to_file(text,"./text.mp3")

if __name__ == '__main__':
    file="E:\北自所工作内容\书本资料文件\文献\下载论文\\NMT-Paper\\2021-Input Augmentation Improves Constrained Beam Searchfor Neural Machine Translation NTT at WAT 2021.pdf"
    read_pdf(file)