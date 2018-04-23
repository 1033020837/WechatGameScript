import img_tool
import pickle
import cv2
import os
import numpy as np
import adb_tool
import time
import tensorflow as tf

#加载knn模型
with open('lr.pickle', 'rb') as fr:
    lr = pickle.load(fr)

def get_result(img, filename):
    res = []
    filenames = img_tool.all(img, filename)
    for filename in filenames:
        img = cv2.imread(os.path.join('SingleChar', filename), 0)
        img = img_tool.v_cut(img)
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

preRes = ''
def one_loop(res):
    if res:
        #adb_tool.tapScreen(292, 1536)
        adb_tool.tapScreenFromPC(77, 490)
    else:
        #adb_tool.tapScreen(788, 1536)
        adb_tool.tapScreenFromPC(230,490)
count = 200
while True:
    start =time.time()
    #img = adb_tool.GetScreenshot()
    img = img_tool.shotFromComputer()
    end = time.time()
    print('截图耗时%f' %(end - start))
    res = get_result(img, '%d.png' % count)
    end2 = time.time()
    print('获取结果耗时%f' % (end2 - end))
    if res == preRes:
        count += 1
        print('repeat')
        continue
    else:
        print(res)
        preRes = res
        one_loop(eval(res))
        count += 1

# count=200
# img = img_tool.shotFromComputer()
# res = get_result(img, '%d.png' % count)
# print(res)

