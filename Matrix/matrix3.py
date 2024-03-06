arr = [[0,2,3],[4,5,0],[7,0,9]]

for i in range(len(arr)):
    for j in range(len(arr[1])):
        if arr[i][j] !=0:
            print(i,j,"  ",arr[i][j])
    # print()