import turtle

i=0


qqq=turtle.Turtle()
#use a nested loop
#use turtle.goto

for i in range(7):
    for i in range(4):
        qqq.forward(100)
        qqq.left(90)
    qqq.pendown()
    qqq.goto(0,i*100)



