#!/usr/bin/env python3
# FileName: etchASketch_2.py
# Description: simple implementation of an Etch A Sketch in Python
#imports
import pygame
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
from pygame.locals import *

BUT1 = "GP0_3"
BUT2 = "GP0_4"
BUT3 = "GP0_5"
BUT4 = "GP0_6"

GPIO.setup(BUT1, GPIO.IN)
GPIO.setup(BUT2, GPIO.IN)
GPIO.setup(BUT3, GPIO.IN)
GPIO.setup(BUT4, GPIO.IN)

# variables
#screenXSize = 600
#screenYSize = 400
#x = 300
#y = 200
screenXSize = input("Set screen width in pixels: ")
screenYSize = input("Set screen height in pixels: ")
x = input("Set cursor X position in pixels: ")
y = input("Set cursor Y position in pixels: ")


pygame.init()
screen = pygame.display.set_mode((screenXSize, screenYSize))

clock = pygame.time.Clock()
screen.fill((255,255,255))

while(1):
    clock.tick(60) #keeps game from exceeding 60 fps
    pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    pygame.display.update()
    if (GPIO.input(BUT1)==0):
        x+=1
    if (GPIO.input(BUT3)==0):
        x-=1
    if (GPIO.input(BUT4)):
        y-=1
    if (GPIO.input(BUT2)):
        y+=1
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            screen.fill((255,255,255))
