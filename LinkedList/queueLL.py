class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class queueLL(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        if self.front == None:
            return True
        
    def enqueue(self,val):
        newNode = Node(val)
        self.count +=1
        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if not self.isEmpty():
            self.count -=1
            if self.front == self.rear:
                self.front = None
                self.rear = None
                return
            else:
                self.front = self.front.next

    def get_first(self):
        if self.isEmpty():
            raise IndentationError(" no data in queue")
        else:
            return self.front.val
        
    def get_rear(self):
        if self.isEmpty():
            raise IndentationError(" no data in queue")
        else:
            return self.rear.val

    def size(self):
        return self.count
    
    def printQueue(self):

        temp = self.front
        while(temp != self.rear ):
            print(temp.val,end=" --> ")
            temp = temp.next
        print(temp.val,end=" --> ")

qu = queueLL()
qu.enqueue(12)
qu.enqueue(24)
qu.enqueue(36)
qu.enqueue(48)
qu.dequeue()
print(qu.get_first(), qu.get_rear())
qu.printQueue()