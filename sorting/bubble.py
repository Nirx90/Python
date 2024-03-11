

# list1 = [8,6,1,4,5,3,7,2]
list1 = [ i*2 for i in range(10000+1,20+1,-1)]
n = len(list1)

def BubbleSort(list1):
    for i in range(n):
        for j in range(n-1-i):
            if list1[j]>list1[j+1]:
                 temp = list1[j+1]
                 list1[j+1]=list1[j]
                 list1[j]=temp
        
    return list1

bs = BubbleSort(list1)
print(bs)