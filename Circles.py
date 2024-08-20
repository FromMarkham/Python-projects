import turtle

qqq=turtle.Turtle()

for a in range(5):
    for i in range(360):
        qqq.forward(a+1)
        qqq.left(1)
    qqq.penup()
    qqq.goto(0,-((a+1)*57.3))
    qqq.pendown()
