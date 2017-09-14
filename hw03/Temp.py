#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus



bus = smbus.SMBus(1)
address1 = 0x49
address2 = 0x4a

while True:
        temp1 = bus.read_byte_data(address1, 0)
        far1 = temp1 * (1.8) + 32
        temp2 = bus.read_byte_data(address2, 0)
        far2 = temp2 * (1.8) + 32
        print("Temperature 1 is")
        print(far1, end = "\n")
        print("Temperature 2 is")
        print(temp2, end = "\n")
        time.sleep(0.25)
        
        

#tmp1 = 'i2cget -y 1 0x49'
#tmp2 = 'i2cget -y 1 0x4a'

#temp = int(tmp1)
#temp1 = int(tmp2)

#far1 = temp1 * (9/5) + 32
#far2 = temp2 * (9/5) + 32

#print(far1)
#print(far2)