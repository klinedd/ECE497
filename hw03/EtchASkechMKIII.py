#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import sys

bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70


#Set buttons as inputs
buttonL = "GP0_3"
buttonR = "GP0_4"
buttonD = "GP0_5"
buttonU = "GP0_6"

#Button/input Setup
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)
GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)

def updateGrid(channel):
    #variables used to keep track of where the "etch-a-sketch" is writing
    global x
    global y
    
    
    #variables used to increment the lines being drawn to create the grid on the screen
    global x1
    global y1
    if channel == "GP0_6":
	    if x < 100*(size-1): x+=100
    if channel == "GP0_5":
    	if x > 50: x-=100
    if channel == "GP0_3":
	    if y > 50: y-=100
    if channel == "GP0_4":
    	if y < 100*(size-1): y+=100

print("Running...")

#Button activates an event handler
GPIO.add_event_detect(buttonL, GPIO.FALLING, callback = updateGrid)
GPIO.add_event_detect(buttonR, GPIO.RISING, callback = updateGrid)
GPIO.add_event_detect(buttonU, GPIO.FALLING, callback = updateGrid)
GPIO.add_event_detect(buttonD, GPIO.RISING, callback = updateGrid)

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# The first byte is GREEN, the second is RED.
grid = [0xf0, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

bus.write_i2c_block_data(matrix, 0, grid)

try:
	while True:
		time.sleep(100)


except KeyboardInterrupt:
	print("Cleaning Up")
	GPIO.cleanup()
GPIO.cleanup()