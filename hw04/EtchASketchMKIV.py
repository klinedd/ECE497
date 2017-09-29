#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import rcpy
import rcpy.encoder as encoder

rcpy.set_state(rcpy.RUNNING)

clear = "PAUSE"

print("Running...")

bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70
delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

GPIO.setup(clear, GPIO.IN)


# The first byte is GREEN, the second is RED.
grid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]


x = 0x01
y = 1

e1 = 0;
e2 = 0;
while 1:
    
    e1_old = e1
    e2_old = e2
    
    time.sleep(.5)
    
    e1 = encoder.get(1)
    e2 = encoder.get(2)
    print('\r {:+6d} | {:+6d}'.format(e1,e2), end = '')
    
    if(e1_old > e1):
        if x < 0x80: x = x << 1
    if (e1_old < e1):
        if x > 0x01: x = x >> 1
    if (e2_old < e2):
        if y < 15: y += 2
    if (e2_old > e2):
       if y > 1: y -= 2
    if not GPIO.input(clear):
        grid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        ]
    
        
    
        
    grid[y] = grid[y] | x
    
    bus.write_i2c_block_data(matrix, 0, grid)

    time.sleep(delay/10)
