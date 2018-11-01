import random
import copy
import numpy
import greedy_search_for_mult_knap
from neighbor_search_for_mult_knap import Neighbor_Searcher


class Tabu_Searcher(Neighbor_Searcher):
    def __init__(self,list_of_stuffs,list_of_knaps,memory_capacity,steps):
        super(Tabu_Searcher,self).__init__(list_of_stuffs,list_of_knaps)
        self.memory_capacity=memory_capacity
        self.memory=[]
        self.steps=steps
    def check_memory(self,state):
        ret=True
        for past in self.memory:
            if (past==state).all():
                ret=False
                break
        return ret
    def add_to_memory(self,state):
        if len(self.memory)<self.memory_capacity:
            self.memory.append(state)
        else:
            self.memory.pop(0)
            self.memory.append(state)

    def tabu_search_one_step(self):
        best_state=numpy.zeros((self.number_of_stuffs,self.number_of_knaps))
        best_value=0
        for i in range(self.number_of_stuffs):
            if self.list_of_stuffs[i].knap_belong!=None:#该stuff已经在背包里的情况
                #1.挪到另一个背包里的情况（如果另一个背包装得下）
                for j in range(self.number_of_knaps):
                    if self.list_of_knaps[j] is self.list_of_stuffs[i].knap_belong:
                        pass
                    else:
                        if self.list_of_stuffs[i].weight<=self.list_of_knaps[j].left_weight:
                            this_state=copy.deepcopy(self.state)
                            this_state[i,self.list_of_stuffs[i].knap_belong.index]=0
                            this_state[i,j]=1
                            if self.check_memory(this_state):#比之前neighbor_search多一个检查memory的过程
                                this_value=self.eval_a_state(this_state)
                                if this_value>=best_value:
                                    best_value=this_value
                                    best_state=this_state
                        else:
                            pass
                
                #2.从现在的背包里挪走 
                this_state=copy.deepcopy(self.state)
                this_state[i,self.list_of_stuffs[i].knap_belong.index]=0
                if self.check_memory(this_state):
                    this_value=self.eval_a_state(this_state)
                    if this_value>=best_value:
                        best_value=this_value
                        best_state=this_state
                    

            else:#该stuff不在背包里的情况 放到所有放的下的包里搜一遍
                for j in range(self.number_of_knaps):
                    if self.list_of_stuffs[i].weight<=self.list_of_knaps[j].left_weight:
                        this_state=copy.deepcopy(self.state)
                        this_state[i,j]=1
                        if self.check_memory(this_state):
                            this_value=self.eval_a_state(this_state)
                            if this_value>=best_value:
                                best_value=this_value
                                best_state=this_state
        
        #现在已经找出best_state,添加到memory并同步到list_of_stuffs和list_of_knaps
        self.add_to_memory(copy.deepcopy(best_state))
        self.state=best_state
        #重新初始化所有knap的剩余weight和stuffs
        for knap in self.list_of_knaps:
            knap.stuffs=[]
            knap.left_weight=knap.max_weight
        #重新初始化所有stuff的knap
        for stuff in self.list_of_stuffs:
            stuff.knap_belong=None
        #按statematrix重新设定状态
        for i in range(self.number_of_stuffs):
            for j in range(self.number_of_knaps):
                if self.state[i,j]==0:
                    pass
                elif self.state[i,j]==1:
                    self.list_of_stuffs[i].knap_belong=self.list_of_knaps[j]
                    self.list_of_knaps[j].stuffs.append(self.list_of_stuffs[i])
                    self.list_of_knaps[j].left_weight-=self.list_of_stuffs[i].weight

        return best_value

    def tabu_search(self):
        count=0
        value_now=self.eval_a_state(self.state)
        while count<=self.steps:
            value_now=self.tabu_search_one_step()
            print("total value: "+str(value_now))
            count+=1
    
if __name__=="__main__":
    number_of_stuffs=100
    number_of_knaps=15
    list_of_stuffs=[]
    list_of_knaps=[]

    for i in range(number_of_stuffs):
        new_stuff=greedy_search_for_mult_knap.Stuff(random.randint(1,10),random.randint(1,10),i)
        list_of_stuffs.append(new_stuff)
    for j in range(number_of_knaps):
        new_knap=greedy_search_for_mult_knap.Knapsack(random.randint(1,15),j)
        list_of_knaps.append(new_knap)
    
    greedy_search_for_mult_knap.greedy_search_for_mult_knap(list_of_stuffs,list_of_knaps)

    searcher=Tabu_Searcher(list_of_stuffs,list_of_knaps,7000,10000)
    searcher.tabu_search()
    
    