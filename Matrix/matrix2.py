arr1 = [[1,2,3],[4,5,6],[7,8,9]]

arr2 = [[11,12,13],[14,15,16],[17,18,19]]

for i in range(len(arr1)):
    for j in range(len(arr1)):
        print(arr1[i][j],end=" ")

    for sp in range(len(arr1)):
        print(" ",end="")

    for k in range(len(arr1)):
        print(arr2[i][k],end=" ")

    for sp in range(len(arr1)):
        print(" ",end="")

    for a in range(len(arr1)):
        sum = arr1[i][a] + arr2[i][a]
        print(sum,end=" ")
    print()