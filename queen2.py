# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:55:14 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:31:37 2017

@author: Administrator
"""
import pygame
import random
import classroom
import time
class Queen:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Chessboard(classroom.Classroom):
    def setbegin(self):
        self.queens=[]
        for i in range(self.n):
            r=random.randint(0,self.n-1)
            q=Queen(i,r)
            self.queens.append(q)
            self.a[i][r]=1
    def show(self):
        for l in self.a:
            print l
    def is_fight(self,q1,q2):
        return q1.y==q2.y or abs(q1.x-q2.x)==abs(q1.y-q2.y)
    def how_fight(self,q,qq):
        lis=0
        for i in [s for s in self.queens if s!=qq]:
            if self.is_fight(q,i):
                lis+=1
        return lis
    def move(self,q):
        futs=[Queen(x,q.y) for x in range(self.n)]
        minf=futs[0]
        for qu in futs:
            if self.how_fight(qu,q)<=self.how_fight(minf,q):
                minf=qu
        if self.how_fight(q,q)==0:
            pass
        elif self.how_fight(q,q) >0:
            q=minf
            self.makea()
    def update(self):
        for q in self.queens:
            self.move(q)
    def show(self):
        for l in self.a:
            print l
        print ''
    def safe(self):
        l=[q for q in self.queens if self.how_fight(q,q)==0]
        return l==[]
    def makea(self):
        self.a=[]
        for i in range(self.n):
            self.a.append([])
        for li in self.a:
            for i in range(self.n):
                li.append(0)
        for q in self.queens:
            self.a[q.x][q.y]=1
BLUE=(0,0,255)
BLACK=(0,0,0)
ge=15
n=60
c=Chessboard(n)
c.setbegin()
#while not c.safe():
#    c.update()
#    c.show()
def drawone(i,j,c):
    if c.a[i][j]!=0:
        pygame.draw.rect(dissurf,BLUE,(i*ge,j*ge,ge,ge))
    else:
        pygame.draw.rect(dissurf,BLACK,(i*ge,j*ge,ge,ge))
def draw(n):
    for i in range(n):
        for j in range(n):
            drawone(i,j,c)
pygame.init()
dissurf=pygame.display.set_mode((n*ge,n*ge))
dissurf.fill(BLACK)
while True:
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    c.update()
    draw(n)
    pygame.display.update()
#    
            
            