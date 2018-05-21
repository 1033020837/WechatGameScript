import img_tool
import pickle
import adb_tool
import time
import util
from config import  config
import os
import cv2


'''创建必要文件夹'''
if not os.path.exists('ScreenShot'):
    os.mkdir('ScreenShot')
if not os.path.exists('SingleChar'):
    os.mkdir('SingleChar')
if config['debug']:
    print("开启了调试模式，请手动答题")
    if not os.path.exists('ScreenShotForTrain'):
        os.mkdir('ScreenShotForTrain')

'''
使用的截屏方法，0代表直接使用adb截屏，1代表使用跨平台的方法从PC截屏，2代表使用windows原生API进行截屏
0方法很慢，最多只能闯到第35关
1方法比较快，有一定几率通关
2方法很快，通关几率更大
'''
shot_type = config['type']

#加载逻辑回归模型
with open('lr.pickle', 'rb') as fr:
    lr = pickle.load(fr)

preRes = '' #保存上一步的表达式，防止因截图过快导致的本次点击了上一张图的答案



'''
一次屏幕点击
'''
def one_tap(res):
    print(eval(res))
    if eval(res):
        if shot_type == 0:
            adb_tool.tapScreen(config['adb_tap_true_x'], config['adb_tap_y'])
        else:
            util.tapScreenFromPC(config['pc_tap_true_x'], config['pc_tap_y'])
    else:
        if shot_type == 0:
            adb_tool.tapScreen(config['adb_tap_false_x'], config['adb_tap_y'])
        else:
            util.tapScreenFromPC(config['pc_tap_false_x'], config['pc_tap_y'])

count = 0   #迭代轮数
while True:
    t1 =time.time()
    if shot_type == 0:
        img = adb_tool.getScreenshot()
    elif shot_type == 1:
        img = util.shotFromComputer()
    else:
        img = util.shotByWinAPI('ScreenShot/%d.png' %count)
    if config['debug']:
        cv2.imwrite('ScreenShotForTrain/%d.png' %int(time.time()), img)
        print("截图成功")
        time.sleep(0.3)
        continue
    #t2= time.time()
    #print('截图耗时%f' %(t2 - t1))
    res = img_tool.get_result(lr, img, '%d.png' % count)
    #t3 = time.time()
    #print('获取结果耗时%f' % (t3 - t2))
    if res == preRes or res == '':
        '''如果表达式和之前的表达式相同，则代表截图重复，可能此时手机已经跳到了下一题，因此不进行点击'''
        count += 1
        print('截图重复')
        continue
    else:
        print(res)
        preRes = res
        one_tap(res)
        count += 1

