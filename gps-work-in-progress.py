from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C

#Import utime library to implement delay
import utime, time


#Used to Store NMEA Sentences
buff = bytearray(255)

#GPS Module UART Connection
gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

print(gps_module)


 


count = 0

while True:
        gps_module.readline()
        buff = str(gps_module.readline())
        print(buff)
        utime.sleep_ms(500)
        count=count+1
        print(count)%               
