import cv2
import adb_tool

"""微信小游戏挑战智力脚本"""

map = {
    1:(int(1920*0.68),int(1020*0.165)),
    2:(int(1920*0.68),int(1020*0.495)),
    3:(int(1920*0.68),int(1020*0.825)),
    4:(int(1920*0.75),int(1020*0.165)),
    5:(int(1920*0.75),int(1020*0.495)),
    6:(int(1920*0.75),int(1020*0.825)),
    7:(int(1920*0.82),int(1020*0.165)),
    8:(int(1920*0.82),int(1020*0.495)),
    9:(int(1920*0.82),int(1020*0.825)),
    0:(int(1920*0.89),int(1020*0.495))
}

start = 102
while start <= 500:
    _str = str(start)
    for char in _str:
        location = map[int(char)]
        adb_tool.tapScreen(location[1],location[0])
    start += 1