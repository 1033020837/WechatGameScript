# from img_tool import  *
#
# for i in range(52,100):
#     img = shotFromComputer()
#     img.save('ScreenShot/%d.png'%i)
#     print(i)
#     time.sleep(1.5)

from pymouse import PyMouse

m = PyMouse()

# x_dim, y_dim = m.screen_size()
# m.click(x_dim//2, y_dim//2, 1)

print(m.position())



