#! /usr/bin/python
##graph.py##
#Released under GNU General Public License v2.0 or higher

from random import *
import pygame,sys

x=640
y=480

class Node:
    color=(0,0,0)
    cx=(0,0)
    cy=(0,0)
    def __init__(self,x,y):
        self.color=(randint(30,240),randint(30,240),randint(30,240))
        self.cx=x
        self.cy=y

pygame.init()
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Graph")
screen.fill((0,0,0))
pygame.display.flip()
running=True
nodes=[]
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                p=Node(event.pos[0],event.pos[1])
                pygame.draw.circle(screen,p.color,(p.cx,p.cy),3,0)
                nodes.append(p)
                pygame.display.flip()
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
            for i in nodes:
            	for j in nodes:
            		pygame.draw.line(screen,(randint(20,230),randint(20,230),randint(20,230)),(i.cx,i.cy),(j.cx,j.cy))
            		pygame.display.flip()
	    nodes=[]
pygame.quit()
