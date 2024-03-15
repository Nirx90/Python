# first decrease j from the end and if value of list[j] is less then pivot element than stop 
# then take i start from pivot+1 and if list[i] is high than pivot stop i
# after this swap list[i] and list[j]
# when k is crossed i than stop
# now i aand j are same 
# then check if list[j] < pi element than swap
# now pi is in middel and all smaller are left side of pi and highes are right side of pi
# now seperate the list from low to pi-1 and pi+1 to high and repeate

# myList = [9, 8, 23, 4, 11, 12, 78, 45, 58, 89]
myList = [11,15,8,13,20,4,3,5,6,9,18,12]
low=0
high=len(myList)-1

def partition(myList,low,high):
    pi = myList[low + high // 2]

    while(low <= high):
        while(myList[low]<pi):
            low += 1

        while(myList[high]>pi):
            high -= 1

        
        if(low <= high):
            myList[low],myList[high] = myList[high],myList[low]
            low += 1

    return low

def quicksort(myList,low,high):
    pi = partition(myList,low,high)
    if low < pi - 1:
        quicksort(myList,low,pi-1)
    if pi < high:
        quicksort(myList,pi,high)

   


q = quicksort(myList,low,high)

print(myList)



