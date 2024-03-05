class Node(object):
    def __init__(self,val,pre=None,next=None):
        self.val = val
        self.pre = pre
        self.next = next

class DoublyLL(object):
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
        newNode.pre = temp

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
        
    def printList_des(self):
        temp = self.get_last()
        while(temp != self.head):
            print(temp.val,end="-->")
            temp = temp.pre
        print(temp.val,end="-->")


    def insert_at_first(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        
        temp = self.head
        self.head = newNode
        newNode.next = temp
        temp.pre = newNode
        
    def insert_after(self,elem,val):
        newNode = Node(val)
        temp = self.head
        while(temp.next != None):
            if(temp.val == elem):
                break
            temp = temp.next
        
        newNode.next = temp.next
        temp.next.pre = newNode
        temp.next = newNode
        newNode.pre = temp

    def insert_at_last(self,val):
        newNode = Node(val)
        temp = self.head
        while(temp.next != None):
            temp = temp.next

        temp.next = newNode
        newNode.pre = temp
        
    def delete_first(self):
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next.pre = None

    def delete_last(self):
        temp = self.head
        while(temp.next.next !=None):
            temp = temp.next
        temp.next = None

    def delete_element(self,elem):
        
        temp = self.head
        while(temp.next !=None):
            if(temp.next.val == elem):
                temp.next = temp.next.next
                temp.next.pre = temp
                break
            temp = temp.next

    
db = DoublyLL()
db.head = Node(21)
db.insert_at_last(56)
db.insert_at_last(90)
db.insert_at_last(34)
db.insert_at_first(11)
# db.insert_after(90,44)

# db.delete_element(21)
db.insert_after(56,88)
db.insert_at_last(208)
db.printList_asc()
print()

# db.delete_first()
# db.delete_first()
db.delete_last()
db.printList_asc()
print()
db.printList_des()
