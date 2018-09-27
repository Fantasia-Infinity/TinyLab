import random
import copy

class M:
    def __init__(self,name,preference_list):
        self.name=name
        self.preference_list=preference_list
        self.pair=None

    def paired(self):
        return self.pair!=None

    def most_prefer_W(self):
        return self.preference_list[0]

class W:
    def __init__(self,name,preference_list):
        self.name=name
        self.preference_list=preference_list
        self.pair=None

    def paired(self):
        return self.pair!=None

    def compare(self,M1,M2):
        for M in self.preference_list:
            if M1==M:
                return M1
            elif M2==M:
                return M2
            else:
                pass

def stable_match(list_of_M,list_of_W):
    single_M=copy.copy(list_of_M)

    def find_by_name(list_of_people,name):
        for i in list_of_people:
            if i.name==name:
                return i
    
    def remove_from_single(M):
        M_name=M.name
        for i in range(len(single_M)):
            if single_M[i].name==M_name:
                single_M.pop(i)
                break
    
    def add_to_single(M):
        single_M.append(M)

    def link(M,W_name):
        W=find_by_name(list_of_W,W_name)
        if(W.paired()):
            pre_M=find_by_name(list_of_M,W.pair)
            winner=W.compare(M,pre_M)
            if winner==M:
                M.pair=W
                W.pair=M
                pre_M.pair=None
                return pre_M
            elif winner==pre_M:
                pass
                return M
        elif(not W.paired()):
            W.pair=M
            M.pair=W
            return None

    for M in list_of_M:
        print("M:"+str(M.name))
        W_name_list=""
        for W_name in M.preference_list:
            W_name_list=W_name_list+str(W_name)+" "
        print(W_name_list)

    print("")

    for W in list_of_W:
        print("W:"+str(W.name))
        M_name_list=""
        for M_name in W.preference_list:
            M_name_list=M_name_list+str(M_name)+" "
        print(M_name_list)

    print("")

    while(single_M!=[]):
        for M in single_M:
            most_prefer_W=M.most_prefer_W()
            loser=link(M,most_prefer_W)
            M.preference_list.pop(0)
            if loser==M:
                pass
            elif loser==None:
                remove_from_single(M)
            else:
                remove_from_single(M)
                add_to_single(loser)
    

    for M in list_of_M:
        print("M:"+str(M.name)+" "+"W:"+str(M.pair.name))



if __name__=="__main__":
    M_list=[]
    W_list=[]
    n=5
    for i in range(n):
        new_prefer_list_M=list(range(n))
        random.shuffle(new_prefer_list_M)
        new_M=M(i,new_prefer_list_M)
        M_list.append(new_M)

        new_prefer_list_W=list(range(n))
        random.shuffle(new_prefer_list_W)
        new_W=W(i,new_prefer_list_W)
        W_list.append(new_W)

    stable_match(M_list,W_list)


