from tkinter import *


window = Tk()
window.geometry("600x400")
window.title("Speed Tracker")
window.configure(background='white')

registerimage = PhotoImage(file="images/rover.png")
v = Label(window, image=registerimage, bd=0).place(x=00, y=30)


accnot=Label(window,font = ('calibri',20, 'bold'),bg="white",foreground = 'Red',text="To accelerate Press ' W ' Key")
accnot.place(x=130, y=340)


window.mainloop()