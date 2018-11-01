import random
import copy
import time
import matplotlib.pyplot as plt
def merge_sort(unsorted_list):

    def devide_one_list_to_two(l):
        lenght=len(l)
        middle=lenght//2
        left=l[0:middle]
        right=l[middle:]
        return (left,right)

    def merge_two_sorted_list(l1,l2):
        if l1==[] or l1==None:
            return l2
        elif l2==[] or l2==None:
            return l1
        else:
            if l1[0]>l2[0]:
                return [l1[0]]+merge_two_sorted_list(l1[1:],l2)
            elif l2[0]>=l1[0]:
                return [l2[0]]+merge_two_sorted_list(l1,l2[1:])
    
    if unsorted_list==[]:
        return []
    elif len(unsorted_list)==1:
        return unsorted_list
    else:
        (left,right)=devide_one_list_to_two(unsorted_list)
        sorted_left=merge_sort(left)
        sorted_right=merge_sort(right)
        return merge_two_sorted_list(sorted_left,sorted_right)

def get_m_total_time_with_merge_sort_lenght_n(n,m):
    total_time=0
    for i in range(m):
        l=list(range(n))
        random.shuffle(l)
        start_time=time.time()
        merge_sort(l)
        end_time=time.time()
        total_time=total_time+(end_time-start_time)
    return total_time


if __name__=="__main__":
    l=list(range(1001))
    random.shuffle(l)
    print(l)

    print(merge_sort(l))
    list_of_y=[]
    list_of_x=[]
    for i in range(0,1000,10):
        list_of_x.append(i)
        list_of_y.append(get_m_total_time_with_merge_sort_lenght_n(i+1,10)*10)
    plt.figure()
    plt.plot(list_of_x,list_of_y)
    plt.savefig("merge.jpg")
    