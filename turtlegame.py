# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:58:19 2017

@author: Fantasia
"""
import turtle as tt
import random
import time
end=290
class Player:
    name=''
    color=''
    state=True
    position=(0,0)
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.t=tt.Turtle()
        self.t.color(color)
    def setname(self,name):
        self.name=name
    def randwalk(self):
        self.t.forward(random.randint(1,10))
        time.sleep(0.1)
    def setcolor(self,color):
        self.color=color
        self.t.color(self.color)
    def setposition(self,a,b):
        self.position=(a,b)
        self.t.penup()
        self.t.setpos(*self.position)
        self.t.pendown()
    def getposition(self):
        return self.position
    def writename(self):
        self.t.write(self.name)
class Game:
    players=[]
    results=[]
    lasty=150
    def setbegin(self):
        begin=tt.Turtle('turtle',1000,False)
        end=tt.Turtle('turtle',1000,False)
        begin.penup()
        end.penup()
        begin.setpos(-290,200)
        end.setpos(290,200)
        begin.pendown()
        end.pendown()
        begin.right(90)
        end.right(90)
        begin.write('START')
        end.write('GAOL')
        begin.forward(400)
        end.forward(400)
    def is_over(self):
        l=[x for x in self.players if x.state]
        if l==[]:
            return True
        else:
            return False
    def addplayer(self,name,color):
        p=Player(name,color)
        p.setposition(-290,self.lasty+30)
        p.t.shape('turtle')
        p.t.write(p.name)
        self.players.append(p)
        self.lasty-=30
    def showresults(self):
        self.results.reverse()
        i=0
        for i in range(len(self.results)):
            print 'the ',i+1,' is',self.results[i].name
    def race(self):
        if (not self.is_over()):
            for p in self.players:
                if p.t.xcor()<289 and p.state:
                    p.randwalk()
                elif p.t.xcor()>289 and p.state:
                    self.results.append(p)
                    p.state=False
                elif (not p.state):
                    pass                   
            self.race()
        else:
            self.showresults()
            return
def jiemian(game):
    while True:
        p=raw_input("AddPlayer?(yes/no)\n")
        if p=='yes':
            name=raw_input("Name?\n")
            color=raw_input("Color?\n")
            game.addplayer(name,color)
        else:
            break
    game.race()
    return
g=Game()
g.setbegin()
jiemian(g)    
            
        

    
