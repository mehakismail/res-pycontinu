import RPi.GPIO as gpio
import time
import serial
import math
global ser
global ser2
import pathlib
import datetime

ser = serial.Serial(
  
   port='/dev/ttyS0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)


while True:

    try:
        line=ser.readline()
        line1=line.rstrip().decode()
        print(line1)
        data = line1.split(',')
        name = data[0]
        age = data[1]
        roll = data[2]

        now = datetime.datetime.now()
    
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                
        path = "//home/pi/modem-data-files/Student_info.csv" 
        p = pathlib.Path(path)

        if p.exists():
            with open(path, "a+") as file:
                file.write(str(name)+','+str(age)+','+str(roll)+','+str(date_time))   
                file.write("\n") 
        
        else:

            with open(path, "a+") as file:
                file.write("Name,Age,Roll,Date")
                file.write(str(name)+','+str(age)+','+str(roll)+','+str(date_time)) 
                file.write("\n")
            
                
    except Exception as e:
        print("error occured: ",e)

        