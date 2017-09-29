from turtle import Turtle,Screen,mainloop

def tree(plist,l,a,f):
    if l>5:
        lst = []
        for p in plist:
            p.forward(l)
            q=p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)

def maketree(x,y):
    window = Screen()
    p=Turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()#隐藏箭头
    p.getscreen().tracer(30,300)
    p.speed(1)
    p.left(90)
    p.penup()
    p.goto(x,y)
    p.pendown()
    t = tree([p],110,65,0.6375)
    window.exitonclick()
def main():
    maketree(0,-200)
main()
