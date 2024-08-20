from customtkinter import *
import time
import datetime
from PIL import Image 
import simpleaudio as sa 

wave_object = sa.WaveObject.from_wave_file('Clicky2 copy.wav')

window=CTk()



window.geometry("375x750")
window.title('Timer, stopwatch and date calculator')
set_appearance_mode("light")



#the lambda part in the article here👇
#https://www.geeksforgeeks.org/how-to-check-which-button-was-clicked-in-tkinter/
file = "Clicky2 copy.wav"
Totalseconds=0
Totalhours=0
Totalminutes=0 
Totaltime=0

hOurs=StringVar()
sEconds=StringVar()
mInutes=StringVar()

hOurs.set('0')
sEconds.set('0')
mInutes.set('0')

def timetracker(timerchange):
    global Totalseconds
    global Totalminutes
    global Totalhours
    global hOurs
    global sEconds
    global mInutes


    if timerchange=="SecondsUp" and Totalseconds>=0 and Totalseconds<59: 

        Totalseconds=Totalseconds+1
        sEconds.set(str(Totalseconds)) 
        play_object = wave_object.play()

        
    if timerchange=="SecondsDown" and Totalseconds>0 and Totalseconds<=59: 
        Totalseconds=Totalseconds-1
        sEconds.set(str(Totalseconds))
        play_object = wave_object.play()
        
    if timerchange=="MinutesUp" and Totalminutes>=0 and Totalminutes<59:
        Totalminutes=Totalminutes+1
        mInutes.set(str(Totalminutes))
        play_object = wave_object.play()
        
    if timerchange=="MinutesDown" and Totalminutes>0 and Totalminutes<=59: 
        Totalminutes=Totalminutes-1
        mInutes.set(str(Totalminutes))
        play_object = wave_object.play()
        
    if timerchange=="HoursUp" and Totalhours>=0 and Totalhours<59: #dont use or
        Totalhours=Totalhours+1
        hOurs.set(str(Totalhours))
        play_object = wave_object.play()
       

    if timerchange=="HoursDown" and Totalhours>0 and Totalhours<=59: #dont use or
        Totalhours=Totalhours-1
        hOurs.set(str(Totalhours))
        play_object = wave_object.play()

    
class labelclass():
    def __init__(self,xcor,ycor,thetext):
        self.Texts=CTkLabel(master=window,textvariable=thetext)
        self.Texts.place(x=xcor,y=ycor)


class labelclass2():
    def __init__(self,xcor,ycor,thetext2):
        self.Texts=CTkLabel(master=window,text=thetext2)
        self.Texts.place(x=xcor,y=ycor)

class progressbarclass():
    def __init__(self):
        progressbar = CTkProgressBar(master=window)
        progressbar.pack(padx=20, pady=10)

class optionsbox():
    def __init__(self):
        combobox=CTkComboBox(master=window)
        combobox.pack(padx=20, pady=10)

#
SecondsUp=CTkButton(window,text="🔺️",width=10,height=10,command=lambda m="SecondsUp": timetracker(m))
SecondsUp.place(x=200,y=200)

SecondsDown=CTkButton(window,text="🔻",width=10,height=10,command=lambda m="SecondsDown": timetracker(m))
SecondsDown.place(x=200,y=280)

MinutesUp=CTkButton(window,text="🔺️",width=10,height=10,command=lambda m="MinutesUp": timetracker(m))
MinutesUp.place(x=160,y=200)

MinutesDown=CTkButton(window,text="🔻",width=10,height=10,command=lambda m="MinutesDown": timetracker(m))
MinutesDown.place(x=160,y=280)

HoursUp=CTkButton(window,text="🔺️",width=10,height=10,command=lambda m="HoursUp": timetracker(m))
HoursUp.place(x=120,y=200)

HoursDown=CTkButton(window,text="🔻",width=10,height=10,command=lambda m="HoursDown": timetracker(m))
HoursDown.place(x=120,y=280)

timerset=CTkButton(window,text="Set timer⏱️",width=30,height=10,command=lambda m="settimer": timetracker(m))
timerset.place(x=120,y=330)

Hours=labelclass(120,240,hOurs)
Minutes=labelclass(160,240,mInutes)
Seconds=labelclass(200,240,sEconds)

Hourslabel=labelclass2(120,305,'Hours')
Minuteslabel=labelclass2(160,305,'Minutes')
Secondslabel=labelclass2(200,305,'Seconds')

window.mainloop()
