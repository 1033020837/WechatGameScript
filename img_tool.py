import cv2
import numpy as np
import config
import os

def cropImg(img):
    """裁剪原始截图"""
    height = img.shape[0]
    img2 = img[int(config.config['exp_area_top_rate'] * height):int(config.config['exp_area_bottom_rate'] * height),:]
    #print('裁剪完毕')
    return  img2


def binaryImg(img):
    """二值化图片"""
    ret, thresh1 = cv2.threshold(img, config.config['binary_threshold'], 255, cv2.THRESH_BINARY)
    # ret, thresh1 = cv2.threshold(img, config.config['binary_threshold'], 255, cv2.THRESH_BINARY_INV)
    #print('二值化完毕')
    return thresh1



def cropAgain(img):
    """再次裁剪"""
    height = img.shape[0]
    img1 = img[0:int(0.5 * height), :]
    img2 = img[int(0.5 * height):height, :]
    #print('再次裁剪完毕')
    return img1, img2

def cutImg(img, filename):
    """水平分割图片"""
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
                if config.config['type'] == 0:
                    sigleCharWidth = config.config['abd_single_char_width']
                else:
                    sigleCharWidth = config.config['pc_single_char_width']
                #为了防止字符粘连,需要在此处宽度进行判断
                if index - start_index > sigleCharWidth * 2:
                    res.append((start_index,start_index + (index - start_index) // 2))
                    res.append((start_index + (index - start_index) // 2, index))
                else:
                    res.append((start_index, index))
                start_index = -1
        index += 1

    imgs = []
    count = 0
    for single_char in res:
        start = single_char[0]
        end = single_char[1]
        sub_img = img[:, start:end]
        sub_img = cv2.resize(sub_img, (120, 240), interpolation=cv2.INTER_CUBIC)
        #cv2.imwrite('SingleChar/%s_%d.png' % (filename, count), sub_img)
        #names.append('%s_%d.png' % (filename, count))
        # cv2.imshow(str(count), sub_img)
        imgs.append(sub_img)
        count += 1
    # cv2.waitKey()
    #print('分割，重新设置大小 %s 完毕' %filename)
    return  imgs

c = 0
def v_cut(img):
    global c
    """竖直方向切割图片"""
    sum_list = np.array(img).sum(axis=1)
    start_index = -1
    end = -1
    index = 0
    for sum in sum_list:
        if sum > 255 * 2:
            start_index = index
            break
        index += 1
    for i in range(1, len(sum_list) + 1):
        if sum_list[-i] > 255 * 2:
            end = len(sum_list) + 1 - i
            break
    img = img[start_index:end, :]
    img = cv2.resize(img, (30, 60), interpolation=cv2.INTER_CUBIC)
    #cv2.imwrite('SingleChar/%d.png' %c, img)
    c += 1
    return img

def all(img, filename):
    """封装对图片的所有操作"""
    img = cropImg(img)
    img = binaryImg(img)

    img1, img2 = cropAgain(img)


    imgs = cutImg(img1, filename + '_1') + cutImg(img2, filename + '_2')

    return imgs

def get_result(lr, img, filename):
    """根据图片的数据获取表达式,lr为逻辑回归模型"""
    res = []
    imgs = all(img, filename)
    for img in imgs:

        img = v_cut(img)




        img = np.array(img).reshape(1, -1)
        img[img == 255] = 1
        y_hat = lr.predict(img)[0]
        if y_hat == 10:
            res.append('+')
        elif y_hat == 11:
            res.append('-')
        elif y_hat == 12:
            res.append('==')
        else:
            res.append(str(y_hat))
    res = ''.join(res)
    return res

#获取用于训练的单个字符
def get_char_for_train():
    if not os.path.exists('SingleCharForTrain'):
        os.mkdir('SingleCharForTrain')

    for f in os.listdir("ScreenShotForTrain"):
        srcImg = cv2.imread(os.path.join("ScreenShotForTrain", f), 0)
        imgs = all(srcImg, f)
        for i,img in enumerate(imgs):
            img = v_cut(img)
            cv2.imwrite('SingleCharForTrain/%s_%d.png' %(f,i), img)
    print("Done!")

import time
import pickle
with open('lr.pickle', 'rb') as fr:
    lr = pickle.load(fr)

if __name__ == '__main__':
    #get_char_for_train()s
    srcImg = cv2.imread('ScreenShot/1.png', 0)
    t1 = time.time()
    #imgs = all(srcImg, "abc")
    res = get_result(lr, srcImg,'s')
    print(res)
    t2 = time.time()
    print(t2 - t1)