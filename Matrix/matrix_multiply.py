li1 = [[1,2,3],[4,5,6],[7,8,9]]

li2 = [[1,2,3],[4,5,6],[7,8,9]]

li3 = []
for i in range(len(li1)):
    ar = []
    
    for j in range(len(li1)):
        temp = 0
        for k in range(len(li1)):
            temp = temp + (li1[i][k] * li2[k][j])
        ar.append(temp)
    li3.append(ar)


for i in range(len(li3)):
    for j in range(len(li3)):
        print(li3[i][j],end=" ")
    print() 
