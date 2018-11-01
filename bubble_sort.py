import random
import time
import matplotlib.pyplot as plt

def bubble_sort(l):
    lenght=len(l)
    for i in range(lenght-1):
        for j in range(lenght-1-i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

def get_m_total_time_with_bubble_sort_lenght_n(n,m):
    total_time=0
    for i in range(m):
        l=list(range(n))
        random.shuffle(l)
        start_time=time.time()
        bubble_sort(l)
        end_time=time.time()
        total_time=total_time+(end_time-start_time)
    return total_time

if __name__=="__main__":
    l=list(range(100))
    random.shuffle(l)
    print(l)
    bubble_sort(l)
    print(l)

    list_of_y=[]
    list_of_x=[]
    for i in range(0,1000,10):
        list_of_x.append(i)
        list_of_y.append(get_m_total_time_with_bubble_sort_lenght_n(i+1,10)*10)
    plt.figure()
    plt.plot(list_of_x,list_of_y)
    plt.savefig("bubble.jpg")