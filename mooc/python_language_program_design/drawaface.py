from graphics import *

win = GraphWin()
face = Circle(Point(100,95),50)
lefteye = Circle(Point(80,80),5)
lefteye.setFill("yellow")
lefteye.setOutline("red")

righteye = Circle(Point(120,80),5)
righteye.setFill("yellow")
righteye.setOutline("red")

mouth = Line(Point(80,110),Point(120,110))

face.draw(win)
mouth.draw(win)
lefteye.draw(win)
righteye.draw(win)
# 等待响应鼠标点击，退出程序
win.getMouse()
win.close()