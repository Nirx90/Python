list1 = [8,6,1,4,5,3,7,2]
# list1 = [ i*2 for i in range(10000+1,20+1,-1)]


def BubbleSort(list1):
    n = len(list1)
    for i in range(1,n):
        flag = True
        for j in range(n-i):
            print(list1)
            if list1[j]>list1[j+1]:
                list1[j+1],list1[j]=list1[j],list1[j+1]
                flag = False
        print(list1)
        if flag is True:
            break 
                 
        
    return list1

bs = BubbleSort(list1)
print(bs)
