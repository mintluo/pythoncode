from graphics import *

def main():
    win = GraphWin("Draw a polygon",300,300)
    win.setCoords(0.0,0.0,300.0,300.0)

    message = Text(Point(150,20),"click five points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)

    polygon = Polygon(p1,p2,p3,p4,p5)
    polygon.setFill("yellow")
    polygon.setOutline("red")
    polygon.draw(win)

    win.getMouse()
    win.close()

if __name__== '__main__':
    main()