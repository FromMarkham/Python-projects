import turtle
from tkinter import *

window=Tk()
window.title("Grapher")
window.geometry("800x80")
function=Entry(window, borderwidth=3)
function.pack()

functionlabel=Label(window, text="Enter the function you wanna graph:")
functionlabel.place(x=35,y=0)

#gui here
#----------------------------------------------------
#🐢here

turtle.screensize(1200,1200, bg="orange")

x=turtle.Turtle()


x.penup()
x.goto(500,0)
x.pendown()

for a in range(11):
    x.goto(500-(a*100),0)
    x.write(x.xcor(), font=("Verdana",20))
    
x.penup()
x.goto(0,500)
x.write("500", font=("Verdana",20))
x.pendown()

for b in range(11):
    x.goto(0,500-(b*100))
    x.write(x.ycor(), font=("Verdana",20))

#for i in range(-500,500):
#    Yvalue=4thfunction
#    if Yvalue>=500 or Yvalue<=-500:
#        ilist.append(i)

#you could also say: if the y coordinate of the turtle is greater then 500
#stop drawing
    #for i in range(-500,500):
        #if eval(function4)<-500 or eval(function4)>500:
            #ilist.append(i)

def graphing():
    function2=function.get()
    
    x.penup()
    xcoord=-500
    x.goto(xcoord,0)
    x.pendown()
    xcounter=0
    xlist=[]

    function6=list(function2)
    
    numberlist=['0','1','2','3','4','5','6','7','8','9',0,1,2,3,4,5,6,7,8,9]
    
    for q in range(len(function6)):
        if q+1>len(function6)-1:
            break 
        
        if function6[q] in numberlist and function6[q+1]=='x':
            xlist.append(q+1)


        #elif q+1==len(function6):
            #break
    
    for f in xlist:
        function6.insert(f,"*")

    function7=''.join(function6)
    print(function7)
    function4=function7.replace("x","i")
    

    for i in range(-500,500):
        if eval(function4)<500 and eval(function4)>-500:
            x.goto(i,eval(function4))
            x.pendown()

        else:
            x.penup()
            x.goto(i,x.ycor())
        

    #x.pendown()
        
    #for i in range(-500,500):
     #       x.goto(i,eval(function3))    




graphbutton=Button(window, text="Graph!📈🤯", command=graphing)
graphbutton.pack()
