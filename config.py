'''
配置文件
'''

config = {
    #使用的截屏方法，0代表直接使用adb截屏，1代表使用跨平台的方法从PC截屏，2代表使用windows原生API进行截屏
    'type': 0,
    #表达式区域的顶部处于整张图片的位置
    'exp_area_top_rate': 0.36,
    #表达式区域的底部处于整张图片的位置
    'exp_area_bottom_rate': 0.56,
    #图片二值化时的阈值
    'binary_threshold': 200,
    #从PC端截屏时，截取区域左上角相对桌面的x坐标
    'projection_x': 10,
    #从PC端截屏时，截取区域左上角相对桌面的y坐标
    'projection_y': 54,
    #从PC端截屏时，截取区域的宽度
    'projection_width': 300,
    #从PC端截屏时，截取区域的高度
    'projection_height': 554,
    #当从PC端截屏时，每次点击手机屏幕后休眠的时间
    'tap_sleep':0.1,
    #使用adb进行截图时点击手机屏幕正确区域的x坐标
    'adb_tap_true_x':292,
    #使用adb进行截图时点击手机屏幕错误区域的x坐标
    'adb_tap_false_x':788,
    #使用adb进行截图时点击手机屏幕正确和错误区域的y坐标
    'adb_tap_y':1536,
    #使用PC进行截图时点击手机屏幕正确区域的x坐标
    'pc_tap_true_x':77,
    #使用PC进行截图时点击手机屏幕错误区域的x坐标
    'pc_tap_false_x':230,
    #使用PC进行截图时点击手机屏幕正确和区域的y坐标
    'pc_tap_y':490
}