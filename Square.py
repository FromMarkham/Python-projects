import turtle

rows=int(input('Enter the no. of rows u want'))
squares=int(input('enter the no. of squares per row u want'))
squarecount=0

qqq=turtle.Turtle()
qqq.backward(300)

for a in range(rows):
    for b in range(squares):
        squarecount=squarecount+1 
        for c in range(4):
            qqq.forward(100)
            qqq.left(90)
        qqq.write(squarecount, font=("Arial",20))
        qqq.forward(100)
    qqq.penup()
    qqq.goto(-300,-a*100-100)
    qqq.pendown()



