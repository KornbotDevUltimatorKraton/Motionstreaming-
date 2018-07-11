import microgear.client as microgear # connecting to the main system by IoT 
import time  # running the time function for date of the the motion 
import serial # Serial communication function 
import logging

appid = "Kornbot"
gearkey = "wBHqON1EtNqlTzu"
gearsecret =  "nt0utSlDrPEOiYOFFfHYJDbEw"
#/////////////////////////////////////////////////////////////////////////////
   #Serial connection function test connection 
try: 
   ser1 = serial.Serial('/dev/ttyUSB0',115200)  # Sensor Shoulder 
except: 
   print('Connection lost please connect module1 USB0')
try: 
   ser2 = serial.Serial('/dev/ttyUSB1',115200) # Sensor Elbow 
except:
   print('Connection lost please connect module2 USB1') 
try: 
   ser3 = serial.Serial('/dev/ttyUSB2',115200) # Sensor wrist  
except: 
    print('Connection lost please connect module3 USB2') 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    print(' ')
def subscription(topic,message):
     print(message)
def disconnect():
    print(' ')

microgear.setalias("VisualStudio")
#microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/Topics")
microgear.connect(False)

while True:
        if(microgear.connected):
                microgear.chat("VisualStudio",ser1.readline()+','+ser2.readline()+','+ser3.readline())
