arr = []

def push(n):
    arr.append(n)

def remove():
    arr.pop(0)

push(5)
push(6)
push(8)
remove()
print(arr)