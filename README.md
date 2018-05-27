# WechatGameScript
    ![](https://img.shields.io/badge/language-python-blue.svg)
    ![](https://travis-ci.org/Alamofire/Alamofire.svg?branch=master)](https://travis-ci.org/Alamofire/Alamofire)


微信小游戏《加减大师》脚本（最高刷到1500关），兼容《加减王者》、《加减大神》以及其他加减系列游戏

<h3>号外号外！</h3>
本脚本最高刷到了《加减大师》第<b>1500</b>关！！！运行最新代码，使用windows原生API截屏的方式。
还有谁？
还有谁？

<h4>游戏说明</h4>

微信小游戏《加减大师》以及其他加减系列的游戏玩法都极其简单，给出一个等式，要玩家在指定时间内判断等式的对错，答对40个就算挑战成功，可以赢取娃娃或现金红包（虽然少的可怜）。

下面以《加减大师》为例进行说明，其他游戏都大同小异。目前我只测试了《加减大师》、《加减王者》、《加减大神》三款游戏，请参考项目中的兼容说明，其他游戏比如《加减大师挑战赛》、《加减大神黄金版》什么的其实都大同小异，无非就是要调一调参数，然后重新训练一下自己的图像识别模型（参考<a href="https://github.com/1033020837/WechatGameScript/issues/3">#3</a>）。

游戏主界面及脚本运行截图如下：
<div align="center">
    <img src="https://github.com/clouduan/WechatGameAutoPlayer/raw/master/Images/PlusSubstractMaster3.png"  width="300" >
     <img src="https://github.com/1033020837/WechatGameScript/blob/master/example.gif" width="300">
</div>

本项目使用Python3编写，下面介绍其实现原理以及使用方法。

<h4>实现原理</h4>

1.截取游戏界面，本项目中提供了三种方案。
 第一种，使用adb命令截取手机屏幕；
 第二种，在PC端和手机端同时运行APowerMirror软件，将手机投屏到电脑上，然后使用Pillow包中的截图方法截取电脑上对应手机屏幕的
 区域。
 第三种，在PC端和手机端同时运行APowerMirror软件，将手机投屏到电脑上，然后使用Python调用windows的原生API截取电脑上对应手机
 屏幕的区域。
 三种截屏方式花费的时间差异很大，第一种每次截屏需要0.7s左右，第二种0.3s左右，第三种0.04s左右。
 
2.提取截屏图片中的表达式区域并进行文字识别，得到表达式字符串。
 由于图片中的表达式区域固定，而且字符规整，因此这一步不是很困难，我仅仅训练了一个简单的逻辑回归模型就得到了非常高的识别正确率。
 
3.根据第二步得到的表达式，调用Python的eval()函数，得到表达式结果的正误，然后点击手机屏幕的相应区域。
点击手机屏幕提供了两种方案，当截屏使用adb命令时，点击手机屏幕也使用adb命令；当截图使用投屏的方案时，点击手机屏幕通过代码点击
电脑上手机的对应区域。
 
 <h4>使用方法</h4>

1.配置ADB
参考以下链接:<a href="https://blog.csdn.net/qq_33337811/article/details/72594178">Win10配置ADB工具</a>

2.安装PyUserInput依赖包，Python3可能无法使用pip直接安装，可以参考以下链接进行安装：
<a href='https://www.cnblogs.com/wangliyuanzcz/p/7999852.html'> Win10 Python3.5安装PyUserInput</a>

3.想办法获得表达式区域顶部和底部的y坐标相对于整个手机屏幕的高度的比例，然后将对应值填入根目录下的config.py文件中的 exp_area_top_rate
和 exp_area_bottom_rate 处。我的手机分辨率是1920*1080，这两个参数分别是0.36和0.56.

4.修改config.py中的type的值，0、1、2分别对应第一、二、三种截屏方案，默认使用第一种即adb命令的截屏方案，建议先尝试一下默认方案。

5.如果选择adb命令的截屏方案，此时你还需要得到游戏主界面中代表正确和错误的点击区域的中心点的大概坐标，并分别填入config.py的
adb_tap_true_x、adb_tap_false_x、adb_tap_y处。由于两个区域高度相同，因此y值只需要填一个。

6.将手机打开调试模式，调到游戏界面，运行 main.py 文件即可。

7.因为adb命令截屏实在太慢，因此程序最多能到达第36关，游戏的回合时间会在36关骤减，导致程序反应不过来。因此，要拿到娃娃，必须使用第二
或者是第三种方案。因此，首先我们得安装APowerMirror软件，软件下载链接：<a href="https://software.airmore.cn/phone-mirror?bd">
 APowerMirror下载</a>。
 
8.打开APowerMirror软件，将手机屏幕投影到电脑上，然后将APowerMirror拉到桌面的一个固定位置，建议拉到左上角。使用QQ的截屏功能或者是
其他方法获取以下参数并填入config.py的对应位置：

    要截取的区域左上角相对桌面的x坐标：projection_x
    
    要截取的区域左上角相对桌面的y坐标：projection_y
    
    截取区域的宽：projection_width
    
    截取区域的高度：projection_height
    
    手机屏幕代表正确的区域的中心相对于桌面的x坐标：pc_tap_true_x
    
    手机屏幕代表错误的区域的中心相对于桌面的x坐标：pc_tap_false_x
    
    手机屏幕代表正确和错误的区域的中心相对于桌面的y坐标：pc_tap_y

9.将config.py中的type设置为1或者2，将手机打开调试模式，调到游戏界面，运行 main.py 文件即可。注意桌面上不要有东西遮挡到手机的投影区域。
  
<h4>相关问题</h4>
1.使用adb命令截屏时无法闯过最后几关
这是无法避免的，因为adb截屏实在很慢。

2.使用第二或者是第三种方案时经常失败
这是多方面因素造成的，比如APowerMirror软件卡断导致截图为空白等，最后能不能得到娃娃是一个玄学问题。

3.字符识别错误
可能是截屏的相关参数设置得不对导致没有截取到正确的区域，或者是因为你的手机屏幕与我的相差很大，导致我的训练数据无法适应你的图片。确定是后者
的，请在本项目的ISSUE中给我留言。

最后，祝你能拿到娃娃！

