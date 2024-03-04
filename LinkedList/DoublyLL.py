class Node(object):
    def __init__(self,val,previous=None,next=None):
        self.val = val
        self.previous = previous
        self.next = next

class Doubly(object):
    def __init__(self):
        self.head = None

    def insert_at_last(self,val):
        if self.head == None:
            self.head = Node(val)
            return 
        newNode = Node(val)
        temp =self.head
        while(temp.next != None):
            temp = temp.next

        
        temp.next = newNode
        newNode.previous = temp

    def get_last(self):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        return temp


    def printList_asc(self):
        temp = self.head
        while(temp.next != None):
            print(temp.val,end="-->")
            temp = temp.next
        print(temp.val,end="-->")
        return temp


    def insert_at_first(self,val):
        if self.head == None:
            newNode = Node(val)
            return
        temp = self.head
        newNode = Node(val)
        self.head = newNode
        self.head.next = temp
        temp.previous = self.head
        

    def printList_des(self):
        temp = self.get_last()
        while(temp != self.head):
            print(temp.val,end="-->")
            temp = temp.previous
        print(temp.val,end="-->")




db = Doubly()
db.head = Node(21)
db.insert_at_last(56)
db.insert_at_last(90)
db.insert_at_last(34)
db.insert_at_first(66)
db.printList_asc()
print()
db.printList_des()
