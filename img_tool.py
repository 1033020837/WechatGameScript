from PIL import Image
import os
import cv2
import numpy as np
from PIL import ImageGrab
import time

def cropImg(img):
    """裁剪原始截图"""
    height = img.shape[0]
    img2 = img[int(0.36 * height):int(0.56 * height),:]
    # img2 = img[int(0.38 * height):int(0.6 * height), int(0.3 * width):int(0.7 * width)]
    #print('裁剪完毕')
    return  img2


def binaryImg(img):
    """二值化图片"""
    ret, thresh1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    #print('二值化完毕')
    return thresh1

def cropAgain(img):
    height = img.shape[0]
    img1 = img[0:int(0.5 * height), :]
    img2 = img[int(0.5 * height):height, :]
    #print('再次裁剪完毕')
    return img1, img2

def cutImg(img, filename):
    sum_list = np.array(img).sum(axis=0)
    start_index = -1
    res = []
    names = []
    index = 0
    for sum in sum_list:
        if sum > 255 * 4:
            if start_index == -1:
                start_index = index
        else:
            if start_index != -1:
                #一个字符的宽度大约在25左右，为了防止字符粘连,需要在此处进行判断
                if index - start_index > 40:
                    res.append((start_index,start_index + (start_index - index) // 2))
                    res.append((start_index + (start_index - index) // 2, index))
                else:
                    res.append((start_index, index))
                print(index - start_index)
                start_index = -1
        index += 1

    count = 0
    for single_char in res:
        start = single_char[0]
        end = single_char[1]
        sub_img = img[:, start:end]
        sub_img = cv2.resize(sub_img, (120, 240), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('SingleChar/%s_%d.png' % (filename, count), sub_img)
        names.append('%s_%d.png' % (filename, count))
        count += 1
    #print('分割，重新设置大小 %s 完毕' %filename)
    print(names)
    return  names

def v_cut(img):
    """竖直方向切割图片，防止图片竖直平移给分类带来的干扰"""
    sum_list = np.array(img).sum(axis=1)
    start_index = -1
    end = -1
    index = 0
    for sum in sum_list:
        if sum > 255 * 2:
            if start_index == -1:
                start_index = index
        else:
            if start_index != -1 or index == len(sum_list):
                end = index
                break
        index += 1
    img = img[start_index:end, :]
    img = cv2.resize(img, (30, 60), interpolation=cv2.INTER_CUBIC)
    return img

def all(img, filename):
    img = cropImg(img)
    img = binaryImg(img)
    img1, img2 = cropAgain(img)
    names = cutImg(img1, filename + '_1') + cutImg(img2, filename + '_2')
    return names


# print(img.size)
# width = img.size[0]
# height = img.size[1]
# img2 = img.crop((0.27 * width, 0.6 * height, 0.73 * width, 0.8 * height))
# img2.show()
# (0.27,0.8) (0.73,0.8)


def shotFromComputer():
    """从PC端截取投影的手机屏幕，节约时间"""
    img = ImageGrab.grab(bbox=(10, 610 - 556, 310, 610))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grayImg
