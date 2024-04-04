# l1 = [7,4,1,5,2,3]
l1 = [1,2,3,8,6,7]

def insertion(l1):
    for i in range(1,len(l1)):
        temp = l1[i]

        j = i-1
        while(j>=0 and temp<l1[j]):
            l1[j+1] = l1[j]
            j-=1
        print(l1)

        l1[j+1]=temp
        print(l1)

    return l1
print(insertion(l1))    
