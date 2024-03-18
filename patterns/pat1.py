n = 5
a = 0
b = 1
for i in range(1,n+1):
    for j in range(i):
        c = a+b
        print(c,end = " ")
        a = b
        b = c     
    print()