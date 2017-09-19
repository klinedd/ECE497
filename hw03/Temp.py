#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

sensor1 = "GP1_3"
sensor2 = "GP1_4"

GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)


def TempAlert(channel)


GPIO.add_event_detect(sensor1, GPIO.BOTH, callback = TempAlert)
GPIO.add_event_detect(sensor2, GPIO.BOTH, callback = TempAlert)

bus = smbus.SMBus(1)
address1 = 0x49
address2 = 0x4a

'i2cset -y  0x49 11 24 w'
'i2cset -y  0x4a 11 24 w'

'i2cset -y  0x49 10 22 w'
'i2cset -y  0x4a 10 22 w'

while True:
        temp1 = bus.read_byte_data(address1, 0)
        far1 = temp1 * (1.8) + 32
        temp2 = bus.read_byte_data(address2, 0)
        far2 = temp2 * (1.8) + 32
        print("Temperature 1 is")
        print(far1, end = "\n")
        print(temp1)
        print("Temperature 2 is")
        print(far2, end = "\n")
        print(temp2)
        time.sleep(0.25)
        
        




