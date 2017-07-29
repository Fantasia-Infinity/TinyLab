# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:09:35 2017

@author: Fantasia
"""
import pygame
import random as rd
class Unit:
    def __init__(self,state,s,x,z,y,sur,xp,yp):
        self.state=state
        self.s=s
        self.x=x
        self.z=z
        self.y=y
        self.sulfur=sur
        self.xp=xp
        self.yp=yp
    def maxnumber(self):
        self.sulfur=max(self.s,self.x,self.z,self.y)
        return self.sulfur
    def radaction(self):
        r=rd.randint(0,3)
        if r==0:
            if self.xp!=0:
                return -1,0,'s'
            else:
                return n-1,0,'s'
        elif r==1:
            if self.xp!=n-1:
                return 1,0,'x'
            else:
                return 1-n,0,'x'
        elif r==2:
            if self.yp!=0:
                return 0,-1,'z'
            else:
                return 0,n-1,'z'
        elif r==3:
            if self.yp!=n-1:
                return 0,1,'y'
            else:
                return 0,1-n,'y'
    def maxaction(self):
        if self.maxnumber()==self.s:
            if self.xp!=0:
                return -1,0,'s'
            else:
                return n-1,0,'s'
        elif self.maxnumber()==self.x:
            if self.xp!=n-1:
                return 1,0,'x'
            else:
                return 1-n,0,'x'
        elif self.maxnumber()==self.z:
            if self.yp!=0:
                return 0,-1,'z'
            else:
                return 0,n-1,'z'
        elif self.maxnumber()==self.y:
            if self.yp!=n-1:
                return 0,1,'y'
            else:
                return 0,1-n,'y'
class Agent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Ground:
    def __init__(self,n):
        self.l=[]
        self.g=[]
        self.n=n
        self.laim=[]
        for i in range(n):
            self.g.append([])
        for line in self.g:
            for i in range(n):
                line.append(0)
        for i in range(n):
            for j in range(n):
                self.g[i][j]=Unit(0,rd.random(),rd.random(),rd.random(),rd.random(),0,i,j)
        self.beginy=n/2
        self.beginx=0
        for i in range(n/2-5,n/2+5):
            for j in range(n/2-5,n/2+5):
                self.g[i][j].state=1
    def addagent(self,x,y):
        self.l.append(Agent(x,y))
    def upper(self,agent):
        a=0.7
        e=0.2
        r=rd.random()
        oldplacex=agent.x
        oldplacey=agent.y
        oldunit=self.g[oldplacex][oldplacey]
        if r>=e:
            action=oldunit.maxaction()
        else:
            action=oldunit.radaction()
        actionname=action[2]
        agent.x+=action[0]
        agent.y+=action[1]
        newsulfur=self.g[agent.x][agent.y].maxnumber()
        if self.g[agent.x][agent.y].state==1:
            newsulfur=100000
        if actionname=='s':
            oldunit.s=(1-a)*oldunit.s+a*newsulfur
        elif actionname=='x':
            oldunit.x=(1-a)*oldunit.s+a*newsulfur
        elif actionname=='z':
            oldunit.z=(1-a)*oldunit.s+a*newsulfur
        elif actionname=='y':
            oldunit.y=(1-a)*oldunit.s+a*newsulfur
        if self.g[agent.x][agent.y].state==1:
            agent.x=self.beginx
            agent.y=self.beginy
    def update(self):
        for agent in self.l:
            self.upper(agent)

n=40
g=Ground(n)
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(0,255,0)
YR=(255,50,50)
ge=6
for i in range(30):
    g.addagent(g.beginx,g.beginy)
def drawone(i,j,c):
    pygame.draw.rect(dissurf,BLACK,(i*ge,j*ge,ge-2,ge-2))
def drawyl(i,j,c):
    pygame.draw.rect(dissurf,YR,(i*ge,j*ge,ge-2,ge-2))
def drawoneaim(i,j,c):
    pygame.draw.rect(dissurf,BLUE,(i*ge,j*ge,ge-2,ge-2))
def drawagent(slime):
    i=slime.x
    j=slime.y
    pygame.draw.rect(dissurf,YELLOW,(i*ge,j*ge,ge-2,ge-2))
pygame.init()
dissurf=pygame.display.set_mode((n*ge,n*ge))
dissurf.fill(BLACK)
while True:
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    g.update()
    rd.shuffle(g.l)
    for i in range(n):
        for j in range(n):
            if g.g[i][j].state==0:
                if g.g[i][j].sulfur<1:
                    drawone(i,j,g)
                else:
                    drawyl(i,j,g)
            else:
                drawoneaim(i,j,g)
    for s in g.l:
        drawagent(s)
    pygame.display.update()
    