class Node(object):
    def __init__(self,val,pre=None,next=None):
        self.val = val
        self.pre = pre
        self.next = next

class DequeueLL(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None
    
    def front_enqueue(self,val):
        newNode = Node(val)
        if self.front == None:
            self.front = newNode
            self.rear = newNode

        else:
            newNode.next = self.front
            self.front.pre = newNode
            self.front = newNode

    def rear_enqueue(self,val):
        newNode = Node(val)
        if self.front == None:
            self.front = newNode
            self.rear = newNode

        elif self.front == self.rear:
            newNode.pre = self.front
            self.front.next = newNode
            self.rear = newNode

        else:
            self.rear.next = newNode
            newNode.pre = self.rear
            self.rear = newNode

    def front_dequeue(self):
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            elif self.front.next == self.rear:
                self.rear.pre = None
                self.front = self.rear
            else:
                self.front = self.front.next
                self.front.pre = None

    def rear_dequeue(self):
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            elif self.rear.pre == self.front:
                self.front.next = None
                self.rear = self.front
            else:
                self.rear = self.rear.pre
                self.rear.next = None

    def printDequeue_next(self):
        temp = self.front
        while(temp):
            print(temp.val,end=" --> ")
            temp = temp.next

    def printDequeue_pre(self):
        temp = self.rear
        while(temp):
            print(temp.val,end=" <-- ")
            temp = temp.pre
        


    
dll = DequeueLL()
dll.front_enqueue(5)
dll.front_enqueue(9)
dll.front_enqueue(27)
dll.rear_enqueue(12)
# dll.rear_enqueue(8)
# dll.rear_enqueue(37)
dll.printDequeue_next()
print()
dll.front_dequeue()
dll.rear_dequeue()
dll.printDequeue_next()
print()
dll.printDequeue_pre()


 