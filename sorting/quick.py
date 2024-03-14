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
low=1
high=len(myList)-1

def quicksort(myList,low,high):
    pi = myList[0]
    i = 1
    j = high
    while(i <= j):
        # print(low,high)
        while(myList[i]<pi):
            i += 1

        while(myList[j]>pi):
            j -= 1

        
        if(i < j):
            myList[i],myList[j] = myList[j],myList[i]

        print(myList)

    if(myList[j]< pi):
        myList[j],myList[0] = myList[0],myList[j]

    # quicksort(myList,0,)
    # quicksort(myList,low+1,high)

q = quicksort(myList,low,high)

print(myList)



