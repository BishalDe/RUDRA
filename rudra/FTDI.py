import serial

def motor2Forward():
    res = 127
    Sabertooth_Serial.write(bytes(chr(res),encoding="utf8"))
    print("Moving Clockwise")

def motor2Reverse():
    res = 1
    Sabertooth_Serial.write(bytes(chr(res),encoding="utf8"))
    print("Moving Anticlockwise")

def motor2Stop():
    res = 64
    Sabertooth_Serial.write(bytes(chr(res),encoding="utf8"))
    print("Motor Stopped")

def motor1Forward():
    res = 255
    Sabertooth_Serial.write(bytes(chr(res),encoding="utf8"))
    print("Moving Clockwise")

def motor1Reverse():
    res = 128
    Sabertooth_Serial.write(bytes(chr(res),encoding="utf8"))
    print("Moving Anticlockwise")

def motor1Stop():
    res = 192
    Sabertooth_Serial.write(bytes(chr(res),encoding="utf8"))
    print("Motor Stopped")


Sabertooth_Serial = serial.Serial(port='/dev/ttyUSB0', baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0
	)

b=input("Enter the motor :- ")
a=input("Enter The action :- ")

while(a!='y'):
    if b=='1':
        if a=='w':
            motor1Forward()
        elif a=='s':
            motor1Reverse()
        elif a=='q':
            motor1Stop()
    elif (b=='2'):
        if a=='w':
            motor2Forward()
        elif a=='s':
            motor2Reverse()
        elif a=='q':
            motor2Stop()

    b=input("Enter the motor :- ")
    a=input("Enter The action :- ")