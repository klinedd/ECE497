Homework 04 Readme file:


MMAP: You can see the memory locations that I found to be useful in the file called MMAP.ods

GPIO via mmap:  The two necessary files for this portion of the homework are beaglebone_gpio.homework
                and gpioThru. To get this file to work properly you must go to cd into /sys/class/gpio
                on the bone and then echo 97 and 98 into export. From there you cd into each gpio and 
                echo 'out' into the direction directory. These are the pins I'm using for the LEDs and
                this then allows the button presses to turn the LEDs on and off.
                
Rotary Encoders:The file to get the rotary encoders to move the LEDs on the board like an etch-a-sketch 
                is EtchASkechMKIV.py. To run this file make sure you have rcpy installed. Instructions
                for that are on the Homework04 assignment doc. 
