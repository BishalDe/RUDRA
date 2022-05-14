from cgitb import text
from tkinter import *
from time import sleep
from time import strftime
import serial


Sabertooth_Serial = serial.Serial(port='/dev/ttyUSB0', baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)

def motor1Forward(val):
    Sabertooth_Serial.write(bytes(chr(val),encoding="utf8"))
    print(val)
   # print("Moving Clockwise")

def motor1Reverse(val):
    Sabertooth_Serial.write(bytes(chr(val),encoding="utf8"))
    #print("Moving Anticlockwise")
    print(val)

def motor1Stop(val):
    Sabertooth_Serial.write(bytes(chr(val),encoding="utf8"))
   # print("Motor Stopped")
    print(val)





window = Tk()
window.geometry("600x400")
window.title("Speed Inputer")
window.configure(background='white')
window.resizable(0, 0)


def exi(event):
    global speed
    speed=64
    motor1Stop(speed)
    acc = " {} ".format(speed)
    accalue.config(text=acc)
  #  print("Acceleration Increased To :- "+str(speed)) 


def increase(event):
    global speed
    if (speed < 127):
        speed = speed+1

        if(speed==64):
            motor1Stop(speed)
        else:
            motor1Forward(speed)

        acc = " {} ".format(speed)
        accalue.config(text=acc)
  #      print("Acceleration Increased To :- "+str(speed)) 



def dec(event):
    global speed
    while(speed > 1 ):
        speed = speed-1

        if(speed==64):
            motor1Stop(speed)
        else:
            motor1Reverse(speed)

        acc = " {} ".format(speed)
        accalue.config(text=acc)
  #      print("Acceleration Decreased To :- "+str(speed))
        break


def time():
    global c
    c = c+1
    cc = " {} sec ".format(str(c))
    string = strftime('%H:%M:%S %p')
    lbll.config(text=string)
    timevalue.config(text=cc)
    lbll.after(1000, time)


speed = 64
c = 0

imagee = PhotoImage(file="images/rover.png")
v = Label(window, image=imagee, bd=0).place(x=00, y=30)

lbll = Label(window, font=('calibri', 20, 'bold'),
             background='white', foreground='purple')
lbll.place(x=0, y=20)

lblll = Label(window, font=('Aerial', 15, 'bold'),
              background='white', foreground='black', text="Clock Time")
lblll.place(x=0, y=0)


accnot = Label(window, font=('calibri', 15, 'bold'), bg="white",
               foreground='Red', text="To accelerate Press ' W ' Key \nTo Deaccelerate Press ' S ' Key")
accnot.place(x=130, y=330)


window.bind("w", increase)
window.bind("s", dec)
window.bind("x", exi)

acclab = Label(window, font=('Aerial', 20, 'bold'), bg="white",
               foreground='Blue', text="Speed Input")
acclab.place(x=370, y=100)

accalue = Label(window, font=('calibri', 22, 'bold'), anchor=CENTER,
                fg="red", bg="Yellow", text=" 64 ", bd=10, cursor="dot")
accalue.place(x=425, y=140)

timelab = Label(window, font=('Aerial', 20, 'bold'),
                bg="white", foreground='Blue', text="Time")
timelab.place(x=415, y=10)

timevalue = Label(window, font=('calibri', 18, 'bold'), anchor=CENTER,
                  fg="white", bg="red", text="   0 sec  ", bd=10, cursor="dot")
timevalue.place(x=425, y=50)



time()

window.mainloop()
