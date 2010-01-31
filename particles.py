#! /usr/bin/python
##particles.py##
#Released under GNU General Public License v2.0 or higher
from random import *
import pygame,sys

x=640
y=480
PARTNUMBER=150

class Particle:
    color=(0,0,0)
    cx=(0,0)
    cy=(0,0)
field=[]
for i in xrange(0,PARTNUMBER):
    a=Particle()
    a.color=(randint(0,240),randint(0,240),randint(0,240))
    a.cx=randint(0,x)
    a.cy=randint(0,y)
    field.append(a)

pygame.init()
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Particles")
screen.fill((0, 0, 0))

for i in field:
    pygame.draw.circle(screen,i.color,(i.cx,i.cy), 3, 0)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0, 0, 0))
    for i in xrange(0,PARTNUMBER):
        if (randint(0,7)%2)==1:
            (field[i]).cx=(field[i]).cx+1
        else:
            (field[i]).cx=(field[i]).cx-1
        if (randint(0,7)%2)==1:
            (field[i]).cy=(field[i]).cy+1
        else:
            (field[i]).cy=(field[i]).cy-1
    screen.fill((0,0,0))
    for i in field:
        pygame.draw.circle(screen,i.color,(i.cx,i.cy), 2, 0)
    pygame.display.flip()
