# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:51:51 2017

@author: Fantasia
"""
import classroom
import random
import pygame
import time
def showstate(p):
    return p.state
def showa(p):
    return p.a
class Cell:
    def __init__(self,x,y,pheromoneA,pheromoneB,state):
        self.state=state
        self.a=pheromoneA
        self.b=pheromoneB
        self.x=x
        self.y=y
class Skin(classroom.Classroom):
    def setbeing(self):
        for i in range(self.n):
            for j in range(self.n):
                self.a[i][j]=Cell(i,j,random.randint(0,10),random.randint(0,10),0.0)
    def upper(self,cell):
        rateta=0.8
        ratetb=0.1
        ratera=0.2001
        raterb=0.2
        delta=0
        deltb=0
        x=0
        for f in self.l:
            delta+=(f(self,cell).a)*rateta/8
            if f(self,cell).state>x:
                delta+=f(self,cell).state*ratera
        delta-=cell.a*rateta
#        if delta>255:
#            delta=255
        for f in self.l:
            deltb+=(f(self,cell).b)*ratetb/8
            if f(self,cell).state<x:
                deltb-=f(self,cell).state*raterb
        deltb-=cell.b*ratetb
#        if deltb>255:
#            deltb=255
        s=delta-deltb
        if abs(cell.state)>255:
            s=0
        return cell.a+delta,cell.b+deltb,cell.state+s
    def update(self):
        newskin=Skin(self.n)
        newskin.setbeing()
        for i in range(self.n):
            for j in range(self.n):
                newskin.a[i][j]=Cell(i,j,self.upper(self.a[i][j])[0],self.upper(self.a[i][j])[1],self.upper(self.a[i][j])[2])
        self.a=newskin.a
    def show(self):
        for i in self.a:
            print map(showa,i) 
        return
n=50
c=Skin(n)
c.setbeing()
ge=5
BLUE=(0,0,255)
BLACK=(0,0,0)
#def drawone(i,j,c):
#    pygame.draw.rect(dissurf,(0,int(c.a[i][j].b),int(c.a[i][j].a)),(i*ge,j*ge,ge-5,ge-5))
def drawone(i,j,c):
    sa=c.a[i][j].state
    s=int((sa+255)/2-10)
    if s>255:
        s=255
    if s<0:
        s=0
    pygame.draw.rect(dissurf,(s,s,s),(i*ge,j*ge,ge-1,ge-1))
#pygame.init()
#dissurf=pygame.display.set_mode((n*ge,n*ge))
#dissurf.fill(BLACK)
#while True:
#    for event in  pygame.event.get():
#        if event.type==pygame.QUIT:
#            pygame.quit()
#    c.update()
#    for i in range(n):
#        for j in range(n):
#            drawone(i,j,c)
#    pygame.display.update()

for i in range(10):
    c.update()
c.show()
"""
Created on Thu Jun 08 14:16:00 2017

@author: Fantasia
"""
import random as rd
import pygame
kwater=0.1
class Unit:
    def __init__(self,high,water,gas):
        kt=0.1
        self.high=high
        self.water=water
        self.gas=gas
        self.temp=high*kt
    def gethigh(self):
        return self.high+kwater*self.water
class Ground:
    def __init__(self,n):
        self.land=[]
        self.n=n
        for i in range(n):
            self.land.append([])
        for l in self.land:
            for i in range(n):
                l.append(0)
    def show(self):
        for l in self.land:
            print [a.gethigh() for a in l]
        print ''
    def randinit(self):
        for i in range(self.n):
            for j in range(self.n):
                self.land[i][j]=Unit(20,0,0)
    def z(self,x,y):
        return x,y-1
    def y(self,x,y):
        if y!=self.n-1:
            return x,y+1
        else:
            return x,0
    def s(self,x,y):
        return x-1,y
    def x(self,x,y):
        if x!=self.n-1:
            return x+1,y
        else:
            return 0,y
    def zs(self,x,y):
        return self.s(*self.z(x,y))
    def zx(self,x,y):
        return self.x(*self.z(x,y))
    def ys(self,x,y):
        return self.s(*self.y(x,y))
    def yx(self,x,y):
        return self.x(*self.y(x,y))
    fl=[z,y,s,x,zs,zx,ys,yx]
    def abalcount(self,x,y):
#        count=0
#        for i in [-1,0,1]:
#            for j in [-1,0,1]:
#                if self.inrange(x+i,y+j):
#                    if self.ground[x+i][y+j].s!=2:
#                        count+=1
#        return count
        return 8
    def uppergas(self,x,y):
        def kuosangas(self,x,y):
            rate=0.9
            deltaout=self.land[x][y].gas*rate
            deltain=0
            for f in self.fl:
                tx,ty=f(self,x,y)
                try:
                    d=self.land[tx][ty].gas*rate/self.abalcount(tx,ty)
                except:
                    d=0.0
                deltain+=d
            self.land[x][y].gas+=deltain
            self.land[x][y].gas-=deltaout
        def ningjiegas(self,x,y):
            t=self.land[x][y].temp
            sg=self.land[x][y].gas
            k=100
            gasdown=(sg/t)*k
            self.land[x][y].gas-=gasdown
            self.land[x][y].water+=gasdown
            if(self.land[x][y].gas<0):
                self.land[x][y].gas=0
        kuosangas(self,x,y)
        ningjiegas(self,x,y)
    def upperwater(self,x,y):
        def flowwater(self,x,y):
            selfhigh=self.land[x][y].gethigh()
            selfwater=self.land[x][y].water
            count=0
            totaldeltah=0
            for f in self.fl:
                nx,ny=f(self,x,y)
                if self.land[nx][ny].gethigh()<selfhigh:
                    totaldeltah+=selfhigh-self.land[nx][ny].gethigh()
                    count+=1
            k=0.5
            totalflow=selfwater*k
            for f in self.fl:
                nx,ny=f(self,x,y)
                kcathe=0.0
                if self.land[nx][ny].gethigh()<selfhigh:
                    deltah=selfhigh-self.land[nx][ny].gethigh()
                    dwater=totalflow*(deltah/totaldeltah)
#                    dland=dwater*kcathe
                    self.land[nx][ny].water+=dwater
#                    self.land[nx][ny].high+=dland
#                    self.land[x][y].high-=dland
            self.land[x][y].water-=totalflow
#        def zhengfawater(self,x,y):
#            t=self.land[x][y].temp
#            sw=self.land[x][y].water
#            k=0.001
#            gasup=sw*t*k
#            waterdown=gasup
#            self.land[x][y].gas+=gasup
#            self.land[x][y].water-+waterdown
#        zhengfawater(self,x,y)
        flowwater(self,x,y)
    def upper(self,x,y):
        self.upperwater(x,y)
        self.uppergas(x,y)
    def update(self):
        l1=range(self.n)
        l2=range(self.n)
        rd.shuffle(l1)
        rd.shuffle(l2)
        for i in l1:#因并不是严格的并行更新 所以打乱更新顺序防止瞬移的bug
            for j in l2:
                self.upper(i,j)

    
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(0,255,0)
RED=(255,0,0)
YR=(200,100,200)
GREY=(100,100,100)
R=(255,255,0)
ge=5
n=50
g=Ground(n)
g.randinit()
for i in range(n):
    for j in range(n):
        g.land[i][j].high=c.a[i][j].a

#g.land[15][35].water=100000
def drawone(i,j,c):
    cnum=0
    if c.land[i][j].water>255:
        cnum=255
    else:
        cnum=c.land[i][j].water
    if cnum>60:
        color=(0,0,cnum)
        pygame.draw.rect(dissurf,color,(i*ge,j*ge,ge-1,ge-1))
    else:
        h=c.land[i][j].high
        if h>255:
            h=255
        pygame.draw.rect(dissurf,(h,h/2,0),(i*ge,j*ge,ge-1,ge-1))
pygame.init()
dissurf=pygame.display.set_mode((n*ge,n*ge))
dissurf.fill(BLACK)
g.land[40][45].water=3000000
while True:
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    for i in range(n):
        for j in range(n):
            drawone(i,j,g)
    g.update()

    pygame.display.update()
    
    
#    
#for i in range(10):
#    g.land[15][15].water=1000000
#    g.update()
#    g.show()

#总流量问题
#最后水会减少的bug