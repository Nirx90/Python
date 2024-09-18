def get_min_cost():
    arr = [7,6,8,6,1,1]

    sum = 0
    while len(arr)>1:
        tempsum = 0
        for i in range(2):
            min = arr[0]
            for j in range(1,len(arr)):
                if arr[j]<min:
                    min = arr[j]
            tempsum += min
            arr.remove(min)

        print(arr)
        print(tempsum)
        arr.append(tempsum)
        print(arr)
        sum += tempsum

    return sum

# n = input(int("enter "))
print(get_min_cost())

