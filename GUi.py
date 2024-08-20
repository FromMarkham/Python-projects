from tkinter import *

qwerty=Tk()

oh=Entry(qwerty)
oh.pack()

nigga=Label(qwerty,text="rrr")
nigga.pack

def texting():
    nigga=Label(qwerty, text=oh.get())
    nigga.pack()


#nigga=Label(qwerty, text="F")

bro=Button(qwerty, text="K", command=texting)



bro.pack()

qwerty.mainloop()
