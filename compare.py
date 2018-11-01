import matplotlib.pyplot as plt
import time
import random
from merge_sort import get_m_total_time_with_merge_sort_lenght_n
from bubble_sort import get_m_total_time_with_bubble_sort_lenght_n

if __name__=="__main__":
    merge_ys=[]
    merge_xs=[]
    bubble_ys=[]
    bubble_xs=[]
    for i in range(0,1000,10):
        merge_xs.append(i)
        merge_ys.append(get_m_total_time_with_merge_sort_lenght_n(i+1,10)*10)
    for j in range(0,1000,10):
        bubble_xs.append(j)
        bubble_ys.append(get_m_total_time_with_bubble_sort_lenght_n(j+1,10)*10)

    plt.figure()
    plt.plot(merge_xs,merge_ys,color="red")
    plt.plot(bubble_xs,bubble_ys,color="green")
    plt.legend()
    plt.savefig("compare.jpg")