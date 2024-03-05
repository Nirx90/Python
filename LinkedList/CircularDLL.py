class Node(object):
    def __init__(self,pre=None,val=None,next=None):
        self.pre = pre
        self.val = val
        self.next = next

class CircularDLL():
    def __init__(self):
        self.head = None

    def insertAtEmpty(self,val):
        if self.head !=None:
            return
        newNode = Node(self.head,val)
        self.head = newNode
        self.head.pre = self.head
        newNode.next = newNode
        newNode.pre = newNode

    def insert_at_first(self,val):
        if self.head == None:
            return self.insertAtEmpty(val)
        
        newNode = Node(self.head,val)
        self.head.next = newNode
        self.head.pre = newNode
        newNode.next = self.head
        newNode.pre = self.head

    def insert_at_head(self,val):
        if self.head == None:
            return self.insertAtEmpty(val)
        
        newNode = Node(val)
        newNode.next = self.head.next



    def printList_asc(self):
        temp = self.head.next
        while(temp.next != self.head):
            print(temp.val,end=" --> ")
            temp = temp.next
        print(temp.val,end=" --> ")

    def printFor(self):
        temp = self.head.next
        for i in range(4):
            print(temp.val,end=" --> ")
            temp = temp.next

cdll = CircularDLL()
cdll.insertAtEmpty(56)
cdll.insert_at_first(21)
cdll.printList_asc()
print()
cdll.printFor()



        