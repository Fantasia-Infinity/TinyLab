# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:24:28 2017

@author: Administrator
"""

import random
def if_rand():
    a=random.randint(0,10)
    return a==1
def cmps(s1,s2):
    if s1.power()<s2.power():
        return -1
    elif s1.power()==s2.power():
        return 0
    elif s1.power()>s2.power():
        return 1
class State:
    def __init__(self,n):#随机初始化，n为皇后数目
        self.l=[]#各个皇后的位置
        self.n=n
        for i in range(n):
            self.l.append(random.randint(0,n-1))
    def show(self):
        board=[]
        for i in range(self.n):
            board.append([])
        for i in range(self.n):
            for j in range(self.n):
                board[i].append(0)
        for i in range(self.n):
            board[i][self.l[i]]=1
        for i in range(self.n):
            print board[i]
        print ''
    def setl(self,lis):
        self.l=lis
    def new(self,s2):#接受另一个状态返回一个交叉后的新状态
        s=State(self.n)
        r=random.randint(1,self.n-1)
        s.l=self.l[:r]+s2.l[r:]
        for i in range(self.n):
            if if_rand():
                s.l[i]=random.randint(0,self.n-1)
        return s
    def power(self):#返回该状态的冲突程度
        n=0
        for i in range(self.n):
            for j in range(self.n):
                if i!=j:
                    if (self.l[i]==self.l[j] or abs(self.l[i]-self.l[j])==abs(i-j)):
                        n+=1
        return n          
k=10
class Env:
    def __init__(self,num_room,num_queen):#随机初始化
        self.livings=[]
        self.nq=num_queen#皇后数目
        self.nr=num_room#状态容量
        for i in range(num_room):
            self.livings.append(State(num_queen))
    def sortstate(self):#按照适应度（power()）给状态们排序返回一个新表
        self.livings=sorted(self.livings,cmp=cmps)       
    def update(self):
        for i in range(len(self.livings)):
            for j in range(i,len(self.livings)):
                self.livings.append(self.livings[i].new(self.livings[j]))
        self.sortstate()#按质量排序
        self.livings=self.livings[:self.nr]#截取最好的十个
        
e=Env(10,10)
i=1
while e.livings[0].power()!=0:
    e.update()
    i+=1
    print i
e.livings[0].show()               
