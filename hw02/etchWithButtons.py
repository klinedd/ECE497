#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import pygame
import sys
from pygame.locals import *


size = input('What X by X size grid do you want? ')
screen = pygame.display.set_mode((100*size,100*size))

x = 0
y = 0
    
x1 = 0
y1 = 0
    
    
BUT1 = "GP0_3"
BUT2 = "GP0_4"
BUT3 = "GP0_5"
BUT4 = "GP0_6"

GPIO.setup(BUT1, GPIO.IN)
GPIO.setup(BUT2, GPIO.IN)
GPIO.setup(BUT3, GPIO.IN)
GPIO.setup(BUT4, GPIO.IN)


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


    
		

GPIO.add_event_detect(BUT1, GPIO.BOTH, callback = updateGrid)
GPIO.add_event_detect(BUT2, GPIO.BOTH, callback = updateGrid)
GPIO.add_event_detect(BUT3, GPIO.BOTH, callback = updateGrid)
GPIO.add_event_detect(BUT4, GPIO.BOTH, callback = updateGrid)



#initializing a blank screen and creating a clock 

pygame.init()
clock = pygame.time.Clock()
screen.fill((255,255,255))



#a continuous while loop so key inputs can always be searched for
while 1:
    #set the frequency on how often to check for user input
    clock.tick(5)

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

    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            screen.fill((255,255,255))






    

