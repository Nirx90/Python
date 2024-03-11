
# arr = [1,10,6,4,7,3,5,2]
arr = [ i*2 for i in range(10000+1,20+1,-1)]

def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                
    return arr

sc = selection(arr)
print(sc)