li1 = []

for i in range(len(li1)):
    temp = []
    for j in range(len(li1)):
       temp.append(int(input("enter number")))
    li1.append(temp)


for i in range(len(li1)):
    for j in range(len(li1)):
        print(li1[i][j],end=" ")
    print()        