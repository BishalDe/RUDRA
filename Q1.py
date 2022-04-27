from cgitb import text
from tkinter import *
from time import sleep
from time import strftime


window = Tk()
window.geometry("600x400")
window.title("Speed Tracker")
window.configure(background='white')
window.resizable(0, 0)


def increase(event):
    global speed, maxacc
    if (speed < 100):
        speed = speed+10
        if(maxacc < speed):
            maxacc = speed
            max = "Highest acc. :- {} m/s2".format(speed)
            maxacclb.config(text=max)
        acc = "{} m/s2 ".format(speed)
        accalue.config(text=acc)
        print("Acceleration Increased To :- "+str(speed))
        speedofr = str(speed*(speed/10))+' m/s '
        speedvalue.config(text=speedofr)


def dec():
    global speed
    while(speed > 0):
        speed = speed-10
        acc = "{} m/s2 ".format(speed)
        accalue.config(text=acc)
        print("Acceleration Decreased To :- "+str(speed))
        speedofr = str(speed*(speed/10))+' m/s '
        speedvalue.config(text=speedofr)
        break


def time():
    global c
    c = c+1
    cc = " {} sec ".format(str(c))
    string = strftime('%H:%M:%S %p')
    lbll.config(text=string)
    timevalue.config(text=cc)
    lbll.after(1000, time)
    lbll.after(1000, dec)


speed = 0
c = 0
maxacc = 0

imagee = PhotoImage(file="images/rover.png")
v = Label(window, image=imagee, bd=0).place(x=00, y=30)

lbll = Label(window, font=('calibri', 20, 'bold'),
             background='white', foreground='purple')
lbll.place(x=0, y=20)

lblll = Label(window, font=('Aerial', 15, 'bold'),
              background='white', foreground='black', text="Clock Time")
lblll.place(x=0, y=0)


accnot = Label(window, font=('calibri', 20, 'bold'), bg="white",
               foreground='Red', text="To accelerate Press ' W ' Key")
accnot.place(x=130, y=340)

window.bind("w", increase)

acclab = Label(window, font=('Aerial', 20, 'bold'), bg="white",
               foreground='Blue', text="Acceleration")
acclab.place(x=370, y=100)

accalue = Label(window, font=('calibri', 22, 'bold'), anchor=CENTER,
                fg="red", bg="Yellow", text="  0 m/s2 ", bd=10, cursor="dot")
accalue.place(x=400, y=140)

timelab = Label(window, font=('Aerial', 20, 'bold'),
                bg="white", foreground='Blue', text="Time")
timelab.place(x=415, y=10)

timevalue = Label(window, font=('calibri', 18, 'bold'), anchor=CENTER,
                  fg="white", bg="red", text="   0 sec  ", bd=10, cursor="dot")
timevalue.place(x=415, y=50)

maxacclb = Label(window, font=('Aerial', 10, 'bold'), bg="white",
                 foreground='Blue', text="Highest acc. :- 0 m/s2")
maxacclb.place(x=400, y=310)

speedlab = Label(window, font=('Aerial', 20, 'bold'),
                 bg="white", foreground='Blue', text="Speed")
speedlab.place(x=415, y=210)

speedvalue = Label(window, font=('calibri', 18, 'bold'), anchor=CENTER,
                   fg="black", bg="orange", text="   0 m/s  ", bd=10, cursor="dot")
speedvalue.place(x=405, y=250)


time()

window.mainloop()
