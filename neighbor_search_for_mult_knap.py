import random
import numpy
import copy
import greedy_search_for_mult_knap

class Neighbor_Searcher:
    def __init__(self,list_of_stuffs,list_of_knaps):
        self.number_of_stuffs=len(list_of_stuffs)
        self.number_of_knaps=len(list_of_knaps)

        self.state=numpy.zeros((self.number_of_stuffs,self.number_of_knaps))
        for i in range(self.number_of_stuffs):
            stuff=list_of_stuffs[i]
            knap=stuff.knap_belong
            if knap!=None:
                self.state[i,stuff.knap_belong.index]=1
        
        self.list_of_stuffs=list_of_stuffs
        self.list_of_knaps=list_of_knaps

    def eval_a_state(self,state):
        sum=0
        for i in range(self.number_of_stuffs):
            for j in range(self.number_of_knaps):
                sum+=state[i,j]*self.list_of_stuffs[i].value
        return sum

    def search_one_step_from_neighbor(self):
        best_state=copy.deepcopy(self.state)
        best_value=self.eval_a_state(best_state)
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
                            this_value=self.eval_a_state(this_state)
                            if this_value>=best_value:
                                best_value=this_value
                                best_state=this_state
                        else:
                            pass
                #2.从现在的背包里挪走 (当然这里完全时浪费计算，不过在之后的禁忌搜索里会有用)
                this_state=copy.deepcopy(self.state)
                this_state[i,self.list_of_stuffs[i].knap_belong.index]=0
                this_value=self.eval_a_state(this_state)
                if this_value>=best_value:
                    best_value=this_value
                    best_state=this_state

            else:#该stuff不在背包里的情况 放到所有放的下的包里搜一遍
                for j in range(self.number_of_knaps):
                    if self.list_of_stuffs[i].weight<=self.list_of_knaps[j].left_weight:
                        this_state=copy.deepcopy(self.state)
                        this_state[i,j]=1
                        this_value=self.eval_a_state(this_state)
                        if this_value>=best_value:
                            best_value=this_value
                            best_state=this_state
        
        #现在已经找出best_state,同步到list_of_stuffs和list_of_knaps
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
    
    def neighbor_search(self):
        value_now=self.eval_a_state(self.state)
        value_last_time=-1
        while value_now>value_last_time:
            value_last_time=value_now
            value_now=self.search_one_step_from_neighbor()
            print("total value: "+str(value_now))

if __name__=="__main__":
    number_of_stuffs=100
    number_of_knaps=10
    list_of_stuffs=[]
    list_of_knaps=[]

    for i in range(number_of_stuffs):
        new_stuff=greedy_search_for_mult_knap.Stuff(random.randint(1,10),random.randint(1,10),i)
        list_of_stuffs.append(new_stuff)
    for j in range(number_of_knaps):
        new_knap=greedy_search_for_mult_knap.Knapsack(random.randint(1,15),j)
        list_of_knaps.append(new_knap)
    
    greedy_search_for_mult_knap.greedy_search_for_mult_knap(list_of_stuffs,list_of_knaps)

    searcher=Neighbor_Searcher(list_of_stuffs,list_of_knaps)
    searcher.neighbor_search()




                



