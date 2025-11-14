# Import machine and OLED libraries 
from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C

# Import utime library to implement delay
import utime, time

# Oled I2C connection
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)


# Used to Store NMEA Sentences
buff = bytearray(255)

# GPS Module UART Connection
gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

print(gps_module)



def convertToDigree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) #degrees
    nexttwodigits = RawAsFloat - float(firstdigits*100) #minutes    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) # to 6 decimal places
    return str(Converted)


# Counbt number of packaet since run start 
count = 1

while True:
        gps_module.readline()
        buff = str(gps_module.readline())
        # print(buff)
        # Print details to shell
        parts = buff.split(',')
        if(parts[0] == "b'$GPGSV"):
                         print(buff)
        if(parts[0] == "b'$GPGGA"):
                print("Got a GPGGA==========================")
                print(buff)
                if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7] and parts[8]):
                    print(count)
                    print("Latitude    : " + parts[2])
                    latitude = convertToDigree(parts[2])
                    longitude = convertToDigree(parts[4])
                    print("Latitude Deg. :" + latitude )
                    print("N/S         : " + parts[3])
                    print("Longitude   : -" + longitude)
                    print("Number of Sats. :" + parts[7])
                    #longitude = convertToDigree(parts[4])
                    
                    oled.fill(0)
                    oled.text("Latitude  : "+str(latitude), 0, 0)
                    oled.text("Longitude : "+str(longitude), 0, 10)
                    oled.text("Satellites: "+ parts[7],0,20,11)
                    oled.show()
                    if (parts[5] == 'W'):
                       longitude = float(longitude)
                       longitude = -longitude
                       #print("Longitude Deg. :" + str(longitude) )
                       oled.fill(0)
                       oled.text("Latitude : "+str(latitude), 0, 0)
                       oled.text("Longitude: "+str(longitude), 0, 10)
                       oled.text("Satellites: "+ parts[7],0,20,11)
                    oled.show()
                count=count+1
        utime.sleep_ms(200)
        #count=count+1
        #print(count)
        
        
 