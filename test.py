from cProfile import label
from tkinter import *
from time import sleep
from time import strftime

window = Tk()
window.geometry("600x400")
window.title("Test")

def test(event):
    global speed
    if (speed<100):
        speed=speed+10
        var.set("Speed "+str(speed)+' m/s')
        print("Speed increased to"+str(speed))
def dec():
    global speed
    while(speed>0):
        speed=speed-10
        var.set("Speed"+str(speed)+'m/s')
        break

def time():
    string = strftime('%H:%M:%S %p')
    lbll.config(text = string)
    lbll.after(1000,time)
    lbll.after(1000,dec)

speed=0
lbll=Label(window, font = ('calibri', 30, 'bold'),background = 'silver',foreground = 'purple')
lbll.pack()
time()

window.bind("w", test)
var = StringVar()
labell = Label( window, anchor = CENTER , fg="black",bg = "Yellow", textvariable = var, bd = 10, cursor = "dot")
var.set("Speed "+str(speed))
labell.pack()


window.mainloop()