#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import pygame, sys
from pygame.locals import *

size = input('What X by X size grid do you want?')
screen = pygame.display.set_mode((100*size,100*size))


pygame.init()

buttonU = "GP0_3"
buttonD = "GPO_4"
buttonL = "GP0_5"
buttonR = "GP0_6"

GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.Setup(buttonL, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)

GPIO.add_event_detect(buttonU, GPIO.BOTH, callback = updateGrid)
GPIO.add_event_detect(buttonD, GPIO.BOTH, callback = updateGrid)
GPIO.add_event_detect(buttonL, GPIO.BOTH, callback = updateGrid)
GPIO.add_event_detect(buttonR, GPIO.BOTH, callback = updateGrid)

GPIO.add_event_detect("PAUSE", GPIO.BOTH, callback = terminate)
GPIO.add_event_detect("MODE", GPIO.BOTH, callback = clear)



#variables used to keep track of where the "etch-a-sketch" is writing
x=0
y=0

#variables used to increment the lines being drawn to create the grid on the screen
x1 = 0
y1 = 0

#initializing a blank screen and creating a clock 
clock = pygame.time.Clock()
screen.fill((255,255,255))

#a continuous while loop so key inputs can always be searched for
while 1:
    #set the frequency on how often to check for user input
    clock.tick(10)

    #creates the rectangle that is drawn where the x and y variables are pointing to
    Rect = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(screen, (0,0,0), Rect)

    #draws the lines for the grid on the screen
    for i in range(size - 1):
        pygame.draw.line(screen, (0,0,0), (x1, y1+(i*100)+100), (x1+100*size, y1+(i*100)+100))
        pygame.draw.line(screen, (0,0,0), (x1+100+(i*100), y1), (x1+100+(i*100), y1+100*size))
    pygame.display.update()

    #looks for when any of the arrow keys are pressed and sets the x and y variables accordingly
    #also checks to make sure the "etch-a-sketch" does not go off the edge of the screen



def updateGrid(channel):
	if channel == "GP0_6":
		 if x < 100*(size-1): x+=100
    	if channel == "GP0_5":
        	if x > 50: x-=100
    	if channel == "GP0_3":
        	if y > 50: y-=100
    	if channel == "GP0_4":
        	if y < 100*(size-1): y+=100



    #event handlers to eithe quit the program or whipe the board back to  a blank grid
def terminate(channel):
	if channel == "PAUSE":
		sys.exit()


def clear(channel):
	if channel == "MODE":
		screen.fill((255,255,255))


try:

        while True:
                time.sleep(100)

except KeyboardInterrupt:
        print("cleaning Up")
        GPIO.cleanup()
GPIO.cleanup()

