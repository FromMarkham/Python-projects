#from playsound import playsound

#for i in range(100):
 #   playsound('Clicky.wav')
 #   print(i)


from customtkinter import *

screen=CTk()

class Timerprogressclass:
    def __init__(self,position,status):
        self.Timerprogress=CTkProgressBar(master=screen,orientation="horizontal")
        self.Timerprogress.set(position) #1=progress bar reached it's end,
        #0= progress bar at the beginning
         
        if status==True:
            self.Timerprogress.pack()

        else:
            pass

Timer=Timerprogressclass(0,True)


screen.mainloop()

