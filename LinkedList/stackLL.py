# stack using singly linked list 
# last in first out

class Node():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class stackLL():
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        if self.head == None:
            return True
        
    def push(self,val):
        newNode = Node(val,self.head)
        self.head = newNode

        self.count+=1
            

    def pop(self):
        if not self.isEmpty():
            data = self.head.val
            self.head = self.head.next
            self.count -= 1
            return data
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.isEmpty():
            return self.head.val
        else:
            raise IndexError("stack is empty")
        
    def printStack(self):
        if self.isEmpty():
            return print("List is empty")
        
        temp = self.head

        while(temp.next != None):
            print(temp.val,end=" --> ")
            temp = temp.next
        print(temp.val,end=" --> ")

    def size(self):
        return self.count

st = stackLL()
st.push(12)
st.push(24)
st.push(36)
st.push(48)
print("poped element", st.pop())
print(st.peek())
st.printStack()