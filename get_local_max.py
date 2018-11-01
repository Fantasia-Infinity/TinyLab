
import random

def get_local_max(list_of_numbers):
    if len(list_of_numbers)==1:
        return list_of_numbers[0]
    elif list_of_numbers[0]>list_of_numbers[1]:
        return list_of_numbers[0]
    elif list_of_numbers[0<list_of_numbers[1]]:
        return get_local_max(list_of_numbers[1:])
#从第一个开始递归的爬山

def showlist(l):
    string=''
    for i in l:
        string=string+str(i)+" "
    print(string)
        

if __name__=="__main__":
    l1=list(range(10))
    random.shuffle(l1)
    showlist(l1)
    print(get_local_max(l1))

    l2=list(range(5))
    random.shuffle(l2)
    showlist(l2)
    print(get_local_max(l2))
