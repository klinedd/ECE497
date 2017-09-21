#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

sensor1 = "GP1_3"
sensor2 = "GP1_4"

GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)

bus = smbus.SMBus(1)
address1 = 0x49
address2 = 0x4a

bus.write_byte_data(address1, 3, 24)
bus.write_byte_data(address1, 2, 22)

bus.write_byte_data(address2, 3, 24)
bus.write_byte_data(address2, 2, 22)

map1 = {sensor1 : address1, sensor2 : address2}
map2 = {sensor1 : 'LeftSensor', sensor2 : 'RightSensor'}


def TempAlert(channel):
        temp = bus.read_byte_data(map1[channel], 0)
        temp = temp*(9/5) + 32
        
        print("****ALERT****: {} is {}\n".format(map2[channel], temp))



GPIO.add_event_detect(sensor1, GPIO.BOTH, callback = TempAlert)
GPIO.add_event_detect(sensor2, GPIO.BOTH, callback = TempAlert)


while True:
        
        temp1 = bus.read_byte_data(address1, 0)
        far1 = temp1 * (1.8) + 32
        temp2 = bus.read_byte_data(address2, 0)
        far2 = temp2 * (1.8) + 32
        print("Temp 1 is {} and Temp 2 is {}".format(far1, far2), end = "\r")
        time.sleep(0.25)
        
        




