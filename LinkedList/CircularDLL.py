class Node(object):
    def __init__(self,val=None,pre=None,next=None):
        self.pre = pre
        self.val = val
        self.next = next

class CircularDLL(object):
    def __init__(self):
        self.head = None

    def insertAtEmpty(self,val):
        if self.head !=None:
            return
        
        newNode = Node(val)
        self.head = newNode
        newNode.next = newNode
        newNode.pre = newNode


    def insert_at_last(self,val):
        if self.head == None:
            return self.insertAtEmpty(val)
        
        newNode = Node(val)
        temp = self.head
        # if temp.next == self.head:
        #     temp.pre = newNode
        #     newNode.next = self.head
        #     newNode.pre = self.head
        #     temp.next = newNode    
        newNode.next = self.head
        newNode.pre = temp.pre
        temp.pre.next = newNode
        temp.pre = newNode

    def insert_at_first(self,val):
        if self.head == None:
            return self.insertAtEmpty(val)
        
        temp = self.head
        newNode = Node(val)
        # if temp.next == self.head:
        #     print("ek j value 6")
        #     newNode.next = self.head
        #     newNode.pre = self.head
        #     temp.pre = newNode
        #     temp.next = newNode
        
        newNode.pre = temp.pre
        temp.pre.next = newNode
        newNode.next = temp
        self.head = newNode
        


        

    def printList_asc(self):
        temp = self.head
        while(temp.next != self.head):
            print(temp.val,end=" --> ")
            temp = temp.next
        print(temp.val,end=" --> ")

    def printFor(self):
        temp = self.head
        for i in range(5):
            print(temp.val,end=" --> ")
            temp = temp.next

cdll = CircularDLL()
cdll.insertAtEmpty(56)
cdll.insert_at_last(12)
cdll.insert_at_last(13)
cdll.insert_at_last(14)
cdll.insert_at_last(26)
cdll.insert_at_last(21)
cdll.insert_at_first(488)
cdll.insert_at_first(236)
cdll.printList_asc()
print()
cdll.printFor()



        