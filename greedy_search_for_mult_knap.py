import random
import copy

class Stuff:
    def __init__(self,weight,value,index):
        self.weight=weight
        self.value=value
        self.proportion=value/weight
        self.knap_belong=None
        self.index=index

class Knapsack:
    def __init__(self,max_weight,index):
        self.max_weight=max_weight
        self.stuffs=[]
        self.left_weight=max_weight
        self.total_value=0
        self.index=index
    def add_stuff(self,stuff):
        stuff.knap_belong=self
        self.stuffs.append(stuff)
        self.left_weight-=stuff.weight
        self.total_value+=stuff.value
        
    def show(self):
        print("left:"+str(self.left_weight)+" value:"+str(self.total_value))

def get_max_pro_stuff_under_w_and_remove_it(list_of_stuffs,w):
    if list_of_stuffs==[]:
        return None
    else:
        stuffs_under_w=[stuff for stuff in list_of_stuffs if stuff.weight<=w]
        if stuffs_under_w==[]:
            return None
        else:
            ret=stuffs_under_w[0]
            for stuff in stuffs_under_w:
                if stuff.proportion>ret.proportion and stuff.weight<=w:
                    ret=stuff
            list_of_stuffs.remove(ret)
            return ret

def get_max_left_weight_knap(list_of_knaps):
    ret=list_of_knaps[0]
    for knap in list_of_knaps:
        if knap.left_weight>ret.left_weight:
            ret=knap
    return ret
                
def show_total_value_of_knaps(list_of_knaps):
    sum=0
    for knap in list_of_knaps:
        sum+=knap.total_value
    print(sum)

def show_all_knaps(list_of_knaps):
    for knap in list_of_knaps:
        knap.show()

def greedy_search_for_mult_knap(list_of_stuffs,list_of_knaps):
    list_of_stuffs_copy=copy.copy(list_of_stuffs)
    chosed_knap=get_max_left_weight_knap(list_of_knaps)
    weight_limit=chosed_knap.left_weight
    chosed_stuff=get_max_pro_stuff_under_w_and_remove_it(list_of_stuffs_copy,weight_limit)
    if chosed_stuff==None:
        show_all_knaps(list_of_knaps)
        print("total value:")
        show_total_value_of_knaps(list_of_knaps)
        return
    else:
        chosed_knap.add_stuff(chosed_stuff)
        print("chosed stuff weight:"+str(chosed_stuff.weight)+" chosed stuff value:"+str(chosed_stuff.value))
        show_all_knaps(list_of_knaps)
        print("total value:")
        show_total_value_of_knaps(list_of_knaps)
        greedy_search_for_mult_knap(list_of_stuffs_copy,list_of_knaps)

if __name__=="__main__":
    number_of_stuffs=100
    number_of_knaps=10
    list_of_stuffs=[]
    list_of_knaps=[]

    for i in range(number_of_stuffs):
        new_stuff=Stuff(random.randint(1,10),random.randint(1,10),i)
        list_of_stuffs.append(new_stuff)
    for j in range(number_of_knaps):
        new_knap=Knapsack(random.randint(1,15),j)
        list_of_knaps.append(new_knap)
    
    greedy_search_for_mult_knap(list_of_stuffs,list_of_knaps)



