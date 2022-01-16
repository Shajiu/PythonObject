# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: tongji_university_java.py
# @Time    : 2022/1/15 20:42
# -*- coding:utf-8 -*-
import os
import time

# 获取当前项目目录
projectDir = os.getcwd()
fileLists = []
# 文件类型
typeList = ['java']


# 遍历项目中的文件夹
def getFile(projectDir):
    global fileLists
    for parent, dirNames, fileNames in os.walk(projectDir):
        for filename in fileNames:
            ext = filename.split('.')[-1]
            if ext in typeList:
                fileLists.append(os.path.join(parent, filename))


# 统计一个文件中代码的行数
def countLine(fileName):
    count = 0
    for file_line in open(fileName,'r',encoding="utf-8").readlines():
        # 不统计空白行
        if file_line != '' and file_line != '\n':
            count += 1
    print(fileName + '----', count)
    return count


if __name__ == '__main__':
    startTime = time.clock()
    getFile(projectDir)
    totalLines = 0
    for typeList in fileLists:
        totalLines = totalLines + countLine(typeList)
    print('Total Lines:', totalLines)
    print('Job Finish! Cost Time: %0.2f second' % (time.clock() - startTime))