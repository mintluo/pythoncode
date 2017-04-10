from turtle import Turtle,Screen

def drawaNum(p,x,num):
    p.penup()
    p.goto(x,0)
    p.pendown()
    p.setheading(0)
    if num==0:
        p.forward(50)
        p.left(90)
        p.forward(100)
        p.left(90)
        p.forward(50)
        p.left(90)
        p.forward(100)
    elif num==1:
        p.penup()
        p.goto(x+50,0)
        p.pendown()
        p.left(90)
        p.forward(100)
    elif num==2:
        p.penup()
        p.goto(x,100)
        p.pendown()
        p.forward(50)
        p.right(90)
        p.forward(50)
        p.right(90)
        p.forward(50)
        p.left(90)
        p.forward(50)
        p.left(90)
        p.forward(50)


def shownums(x,y):
    window = Screen()
    p=Turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()#隐藏箭头
    #p.getscreen().tracer(30,300)
    p.speed(1)
    p.penup()
    p.goto(x,y)
    p.pendown()
    drawaNum(p,x,1)
    drawaNum(p,x+120,0)
    drawaNum(p,x+240,2)
    window.exitonclick()
def main():
    shownums(0,0)
main()
