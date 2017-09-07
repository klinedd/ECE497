#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

pygame.init()

size = input('What X by X size grid do you want?')
screen = pygame.display.set_mode((100*size,100*size))

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
    clock.tick(13)

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
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if x < 100*(size-1): x+=100
    if key[pygame.K_LEFT]:
        if x > 50: x-=100
    if key[pygame.K_UP]:
        if y > 50: y-=100
    if key[pygame.K_DOWN]:
        if y < 100*(size-1): y+=100

    #event handlers to eithe quit the program or whipe the board back to  a blank grid
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))
