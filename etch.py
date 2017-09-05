#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

size = input('What X by X size grid do you want?')
screen = pygame.display.set_mode((100*size,100*size))

x=0
y=0
x1 = 0
y1 = 0

clock = pygame.time.Clock()
screen.fill((255,255,255))

while 1:
    clock.tick(13)
    Rect = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(screen, (0,0,0), Rect)
    for i in range(size - 1):
        pygame.draw.line(screen, (0,0,0), (x1, y1+(i*100)+100), (x1+100*size, y1+(i*100)+100))
        pygame.draw.line(screen, (0,0,0), (x1+100+(i*100), y1), (x1+100+(i*100), y1+100*size))
    pygame.display.update()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if x < 100*(size-1): x+=100
    if key[pygame.K_LEFT]:
        if x > 50: x-=100
    if key[pygame.K_UP]:
        if y > 50: y-=100
    if key[pygame.K_DOWN]:
        if y < 100*(size-1): y+=100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))


