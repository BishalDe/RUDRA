from cgitb import text
from tkinter import *


window = Tk()
window.geometry("600x400")
window.title("Speed Tracker")
window.configure(background='white')

def test(event):
    global speed
    if (speed<100):
        speed=speed+10
        acc="{} m/s2".format(speed)
        accalue.config(text=acc)
        print("Acceleration Increased To :- "+str(speed))

speed=0

imagee = PhotoImage(file="images/rover.png")
v = Label(window, image=imagee, bd=0).place(x=00, y=30)


accnot=Label(window,font = ('calibri',20, 'bold'),bg="white",foreground = 'Red',text="To accelerate Press ' W ' Key")
accnot.place(x=130, y=340)

window.bind("w", test)

acclab = Label(window,font = ('Aerial',20, 'bold'),bg="white",foreground = 'Blue',text="Acceleration")
acclab.place(x=370, y=100)

accalue = Label( window,font = ('calibri',22, 'bold'), anchor = CENTER , fg="red",bg = "Yellow", text=" 0 m/s2", bd = 10, cursor = "dot")
accalue.place(x=390, y=140)


window.mainloop()