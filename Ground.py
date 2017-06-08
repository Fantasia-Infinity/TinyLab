# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:16:00 2017

@author: Fantasia
"""
import random as rd
class Unit:
    def __init__(self,high,water,gas):
        kt=0.1
        self.high=high
        self.water=water
        self.gas=gas
        self.tem=high*kt
    def gethigh(self):
        kwater=0.1
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
    def randinit(self):
        for i in range(self.n):
            for j in range(self.n):
                self.land[i][j]=Unit(rd.randint(0,100),0,0)
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
    def upperwater(self,x,y):
    def abalcount(self,x,y):
#        count=0
#        for i in [-1,0,1]:
#            for j in [-1,0,1]:
#                if self.inrange(x+i,y+j):
#                    if self.ground[x+i][y+j].s!=2:
#                        count+=1
#        return count
        return 8
    def kuosangas(self,x,y):
        rate=0.9
        deltaout=self.ground[x][y].gas*rate
        deltain=0
        for f in self.fl:
            tx,ty=f(self,x,y)
            try:
                d=self.ground[tx][ty].gas*rate/self.abalcount(tx,ty)
            except:
                d=0.0
            deltain+=d
        self.ground[x][y].gas+=deltain
        self.ground[x][y].gas-=deltaout
    def ningjiegas(self,x,y):
        t=self.land[x][y].temp
        
        
    
    
    
    
    
    
    
    
#g=Ground(10)
#g.randinit()

