# arr = [1,10,6,4,7,3,5,2]
arr = [1,2,3,4,5,7,6,8]
# arr = [ i*2 for i in range(20000+1,20+1,-1)]

def selection(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
        
        arr[i],arr[min] = arr[min],arr[i]            
    return arr

sc = selection(arr)
print(sc)
