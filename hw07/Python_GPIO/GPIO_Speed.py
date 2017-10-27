#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

GP1_3 = "GP1_3"
GP1_4 = "GP1_4"

GPIO.setup(GP1_3, GPIO.IN)
GPIO.setup(GP1_4, GPIO.OUT)

map = {GP1_3 : GP1_4}


def run(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + "Toggled")
    
print("Running...")

GPIO.add_event_detect(GP1_3, GPIO.BOTH, callback = run)

try:
	while True:
		time.sleep(100)


except KeyboardInterrupt:
	print("Cleaning Up")
	GPIO.cleanup()
GPIO.cleanup()