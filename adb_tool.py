import os
import time
import subprocess
import sys
from io import BytesIO
import cv2
from PIL import Image
import numpy as np
from pymouse import PyMouse

def getScreenShoot(filename = 'shoot.png'):
    """获取手机屏幕截图"""
    cmd1 = 'adb shell /system/bin/screencap -p /sdcard/screenshot.png'
    cmd2 = 'adb pull /sdcard/screenshot.png ScreenShoot/%s' %(filename)
    t1 = time.time()
    os.system(cmd1)
    t2 = time.time()
    os.system(cmd2)
    t3 = time.time()
    print('t2-t1  %f' % (t2 - t1))
    print('t3-t2  %f' % (t3 - t2))


def tapScreen(x, y):
    cmd = "adb shell input tap %f %f" %(x,y)
    p = os.popen(cmd)
    print(p.read())

m = PyMouse()

def tapScreenFromPC(x, y):
    """从电脑上点击手机投影区域"""
    m.click(int(x), int(y), 1)
    time.sleep(0.1)


def GetScreenshot():
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE, bufsize=1)
    # t2 = time.time()
    #t1 = time.time()
    screenshot = process.stdout.read()
    if screenshot == b'':
        print('Please make sure you can run adb commands successfully.')
        os._exit(0)
    #t2 = time.time()
    # 直接在内存中读写，节约时间
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\n', b'\n')
    #t3 = time.time()
    #print('t2-t1  %f' %(t2-t1))
    # print('t3-t2  %f' % (t3 - t2))
    #allTime.append(t2-t1)
    return cv2.imdecode(np.fromstring(screenshot, np.uint8), 0)

#tapScreen(250,250)
#GetScreenshot()

#getScreenShoot()
