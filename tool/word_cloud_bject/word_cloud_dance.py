# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: word_cloud_dance.py
# @Time    : 2022/1/4 21:54

"""
功能：
    如何AI制造程序猿与仙女舞蹈？
"""
'''
导入模块
'''
import os
import re
import cv2
from pixellib.semantic import semantic_segmentation
import matplotlib.pyplot as plt  # 数据可视化
import jieba  # 词语切割
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云、颜色生成器、停止词
import numpy as np  # 科学计算
from PIL import Image  # 处理图片
import moviepy.editor as mpy  # 添加音频
from moviepy.editor import CompositeAudioClip, VideoFileClip, AudioFileClip  # mp4中提取音乐


def install():
    libs = {"lxml", "requests", "pandas", "numpy", "you-get", "opencv-python", "pandas", "fake_useragent", "matplotlib",
            "moviepy", "pixellib"}
    try:
        for lib in libs:
            os.system(f"pip install -i https://pypi.doubanio.com/simple/ {lib}")
            print(lib + "下载完毕");
    except:
        print(lib + "下载失败")


'''
视频处理
功能:
     从B站下载舞蹈视频;
使用说明：
     可以使用you-get，用它可以下载视频，先安装 pip install you-get；找到想要下载视频的链接，使用如下指令，便可下载。
     you-get -i https://www.bilibili.com/video/BV11C4y1h7nX

'''

'''
视频分割
    使用opencv，将视频分割为图片，本分截取了800张图片用于制作词云，Opencv中通过VideoCaptrue类对视频进行读取操作以及调用摄像头，具体代码如下。
'''


def splitFrames():
    videoFileName = "E:\word_cloud_bject\PrimaryVideoDisplay\\wudao.mp4"
    cap = cv2.VideoCapture(videoFileName)  # 打开视频文件
    num = 1
    while True:
        # success 表示是否成功，data是当前帧的图像数据；.read读取一帧图像，移动到下一帧
        success, img = cap.read()
        if not success:
            break
        img_new = img
        # cv2.flip(img,0,img_new)
        dst_im = cv2.flip(img_new, 1)  # 原型：cv2.flip(src, flipCode[, dst]) → dst  flipCode表示对称轴 0：x轴  1：y轴.  -1：both
        img_new = cv2.transpose(dst_im)
        width = int(img_new.shape[1] * 0.5)
        height = int(img_new.shape[0] * 0.5)
        dim = (width, height)
        img_new = cv2.resize(img_new, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite('E:\word_cloud_bject\ImageSegmentation\\' + str(num) + ".jpg", img_new)
        print(num)
        num = num + 1
    cap.release()


'''
人像分割
   使用mask_rcnn_coco进行图像分割，创建一个分割的应用，具体如下代码所示。
'''
def body_segmentation():
    segment_image = semantic_segmentation()
    segment_image.load_pascalvoc_model(
        "E:\Python_Projects\ObjectDetection\models\deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\ImageSegmentation"):
        for file_name in file_list:
            segment_image.segmentAsPascalvoc(os.path.join(path, file_name),
                                             output_image_name="E:\word_cloud_bject\SplitImage\\" + file_name)


def segmentation_to_binaryzation():
    '''
    功能：将分割图像转换为二值化图
    :return:
    '''
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\SplitImage"):
        for file_name in file_list:
            img = cv2.imread(os.path.join(path, file_name))
            Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(Grayimg, 12, 255, cv2.THRESH_BINARY)
            cv2.imwrite("E:\word_cloud_bject\Binaryzation\\" + file_name, thresh)


def one_to_three():
    '''
    功能：单通道图像转换为三通道的图像
    :return:
    '''
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\Binaryzation"):
        for file_name in file_list:
            img = cv2.imread(os.path.join(path, file_name), 1)
            # 彩色图像转换为灰度图像（3通道变为1通道）
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 最大图像灰度值减去原图像，即可得到反转的图像
            dst = 255 - gray
            cv2.imwrite("E:\word_cloud_bject\OneToThree\\" + file_name, dst)


def black_to_red():
    '''
    功能： 黑色转换为红色
    :return:
    '''
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\OneToThree"):
        for file_name in file_list:
            src = cv2.imread(os.path.join(path, file_name), 0)
            src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2RGB)
            src_RGB[np.where((src_RGB == [0, 0, 0]).all(axis=2))] = [0, 0, 255]
            cv2.imwrite("E:\word_cloud_bject\BlackToRed\\" + file_name, src_RGB)


def rotate():
    '''
    功能：将图像向右旋转了90度
    :return:
    '''
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\BlackToRed"):
        for file_name in file_list:
            img = cv2.imread(os.path.join(path, file_name))
            img90 = np.rot90(img, -1)  # 对图像矩阵顺时针旋转90度
            cv2.imwrite("E:\word_cloud_bject\Rotate\\" + file_name, img90)  # 保存旋转后的图像


"""
生成词云图
    首先进行分词，添加停用词和自定义词组，
"""

def word_cloud():
    '''
    功能: 生成词云
    :return:
    '''
    jieba.load_userdict("E:\word_cloud_bject\Corpus\\barrages.txt")
    result_list = []
    with open('E:\word_cloud_bject\Corpus\\cn_stopwords.txt', 'r', encoding='utf-8') as f:
        con = f.read().split('\n')
        stop_words = set()
        for i in con:
            stop_words.add(i)
    with open('E:\word_cloud_bject\Corpus\\barrages.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
    new_data = "/".join(new_data)
    # 文本分词
    seg_list_exact = jieba.cut(new_data, cut_all=True)
    for word in seg_list_exact:
        # 设置停用词并去除单个词
        if word not in stop_words and len(word) > 1:
            result_list.append(word)
    space_list = ' '.join(result_list)  # 空格链接词语
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\Rotate"):
        for file_name in file_list:
            backgroud = np.array(Image.open(os.path.join(path, file_name)))
            wc = WordCloud(width=1400, height=2200,
                           background_color='white',
                           mode='RGB',
                           mask=backgroud,  # 添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
                           max_words=500,
                           stopwords=STOPWORDS.add('老年人'),  # 内置的屏蔽词,并添加自己设置的词语
                           font_path='C:\Windows\Fonts\STZHONGS.ttf',
                           max_font_size=150,
                           relative_scaling=0.6,  # 设置字体大小与词频的关联程度为0.4
                           random_state=50,
                           scale=2
                           ).generate(space_list)
            image_color = ImageColorGenerator(backgroud)  # 设置生成词云的颜色，如去掉这两行则字体为默认颜色
            wc.recolor(color_func=image_color)
            plt.imshow(wc)  # 显示词云
            plt.axis('off')  # 关闭x,y轴
            # plt.show()                     # 显示
            wc.to_file("E:\word_cloud_bject\WordCloud\\" + file_name)  # 保存词云图




'''
图片合成
   如官方文档所介绍的，moviepy是一个用于视频编辑Python库，可以切割、拼接、标题插入，视频合成（即非线性编辑），
   进行视频处理和自定义效果的设计。总的来说，可以很方便自由地处理视频、图片等文件。
'''


def photofunia():
    '''
    通过多张图片(jpg)合成视频(mp4)
    :return:
    '''
    # 输出视频的保存路径
    video_dir = "E:\word_cloud_bject\GeneratedVideo\\Result1.mp4"
    # 帧率
    fps = 30
    # 图片尺寸
    img_size = (1000, 1080)
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')  # opencv3.0 mp4会有警告但可以播放
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
    for path, dir_list, file_list in os.walk(r"E:\word_cloud_bject\WordCloud"):
        for file_name in file_list:
            frame = cv2.imread(os.path.join(path, file_name))
            frame = cv2.resize(frame, img_size)  # 生成视频   图片尺寸和设定尺寸相同
            videoWriter.write(frame)  # 写进视频里
            print(f'======== 按照视频顺序第{file_name}张图片合进视频 ========')
        videoWriter.release()  # 释放资源


def movie():
    '''
    功能: 从视频(mp4)中提取背景音乐
    :return:
    '''
    video = VideoFileClip('E:\Python_Projects\word_cloud_bject\PrimaryVideoDisplay\\wudao.mp4')
    audio = video.audio
    audio.write_audiofile('E:\Python_Projects\word_cloud_bject\MusicalAudioChimer\\test.mp3')


def add_audio_track():
    '''
    功能：向视频(mp4)中加载背景音乐(mp3)
    :return:
    '''
    # 读取词云视频
    my_clip = mpy.VideoFileClip('E:\Python_Projects\word_cloud_bject\GeneratedVideo\\Result1.mp4')
    # 截取背景音乐
    audio_background = mpy.AudioFileClip('E:\Python_Projects\word_cloud_bject\MusicalAudioChimer\\test.mp3').subclip(0,
                                                                                                                     32)
    # audio_background.write_audiofile('E:\Python_Projects\word_cloud_bject\MusicalAudioChimer\\test.mp3')
    # 视频中插入音频
    final_clip = my_clip.set_audio(audio_background)
    # 保存为最终的视频   动听的音乐！漂亮小姐姐词云跳舞视频！
    final_clip.write_videofile('E:\Python_Projects\word_cloud_bject\GeneratedVideo\\final_video.mp4', audio_codec='aac')


def transform_mp4_gif():
    """
    功能: mp4转gif（便于markdown中直接加载视频）
    ![](https://gitee.com/turbo-studio/image/raw/master/image/20210215225951.gif)
    :return:
    """
    import moviepy.editor as mpy
    # 视频文件的本地路径
    content = mpy.VideoFileClip("E:\Python_Projects\\tool\\aaa.avi")
    # 剪辑0分0秒到0分4秒的片段。resize为修改清晰度
    c1 = content.subclip((0, 0), (0, 4)).resize((480, 320))
    # 将片段保存为gif图到python的默认路径
    c1.write_gif("E:\Python_Projects\\tool\\gav24.gif")

if __name__ == '__main__':
    # 想执行那个函数就直接写函数名称即可
    transform_mp4_gif()
