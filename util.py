'''
一些辅助方法
'''

import win32gui, win32ui, win32con
import cv2
from pymouse import PyMouse
import time
from PIL import ImageGrab
import numpy as np
from config import config
import os

def shotFromComputer():
    """从PC端截取投影的手机屏幕，节约时间"""
    img = ImageGrab.grab(bbox=(config['projection_x'], config['projection_y'], config['projection_x'] +
                               config['projection_width'], config['projection_y'] + config['projection_height']))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grayImg



def shotByWinAPI(filename):
    """使用windows原生API截屏，快的一匹"""
    w = config['projection_width']
    h = config['projection_height']
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (config['projection_x'], config['projection_y']), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    img = cv2.imread(filename, 0)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    #os.remove(filename)
    return img

m = PyMouse()
def tapScreenFromPC(x, y):
    """从电脑上点击手机投影区域"""
    m.click(int(x), int(y), 1)
    #time.sleep(config['tap_sleep'])

