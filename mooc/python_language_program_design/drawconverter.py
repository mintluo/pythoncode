from graphics import *

def main():
    win = GraphWin("Draw a converter",400,300)
    win.setCoords(0.0,0.0,3.0,4.0)




    message = Text(Point(1,3),"Temperature C")
    message.draw(win)
    Text(Point(1, 1), "Temperature F").draw(win)

    input = Entry(Point(2,3),5)
    input.setText("0.0")
    input.draw(win)

    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5, 2), "do it")
    button.draw(win)

    polygon = Rectangle(Point(1,1.5),Point(2,2.5))
    #polygon.setFill("yellow")
    polygon.setOutline("red")
    polygon.draw(win)

    win.getMouse()
    cel = eval(input.getText())
    fah = 9.0/5.0*cel+32.0
    output.setText(fah)
    button.setText("quit")

    win.getMouse()
    win.close()

if __name__== '__main__':
    main()