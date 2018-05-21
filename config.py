'''
配置文件
'''

config = {
    #debug模式，如果开启，则会只进行截屏而不答题，积累训练图片，请手动答题
    'debug': False,
    #使用的截屏方法，0代表直接使用adb截屏，1代表使用跨平台的方法从PC截屏，2代表使用windows原生API进行截屏
    'type': 3,
    #表达式区域的顶部处于整张图片的位置
    'exp_area_top_rate': 0.36,
    #表达式区域的底部处于整张图片的位置
    'exp_area_bottom_rate': 0.56,
    #图片二值化时的阈值
    'binary_threshold': 200,
    #'binary_threshold': 150,
    #从PC端截屏时，截取区域左上角相对桌面的x坐标
    'projection_x': 10,
    #从PC端截屏时，截取区域左上角相对桌面的y坐标
    'projection_y': 54,
    #从PC端截屏时，截取区域的宽度
    'projection_width': 300,
    #从PC端截屏时，截取区域的高度
    'projection_height': 554,
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
    'pc_tap_y':490,
    #使用adb截屏时一个字符的宽度
    'abd_single_char_width':80,
    #使用PC截屏时一个字符的宽度
    'pc_single_char_width':25,
    #游戏一开始每次截图重复时休眠的时间，随着轮数的增加而衰减
    'sleep_when_repeat':0.25,
}