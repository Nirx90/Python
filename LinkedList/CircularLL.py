class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class circularLL(object):
    def __init__(self):
        self.last = None

    def isEmpty(self):
        if self.last == None:
            return True

    def insertAtEmpty(self, val):
        if self.last != None:
            return None 
        
        newNode = Node(val)
        self.last = newNode
        self.last.next = self.last


    def insert_at_first(self, val):
        if self.isEmpty:
            return self.insertAtEmpty(val)
        
        newNode = Node(val)

        newNode.next = self.last.next
        self.last.next = newNode

    def insert_after(self,elem,val):
        newNode = Node(val)
        temp = self.last
        while(temp.next!=self.last):
            if(temp.val == elem):
                 break
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode

    def delete_data(self,elem):
        temp = self.last
        while(temp.next.next !=self.last):
            if(temp.next.val == elem):
                temp.next = temp.next.next
            temp = temp.next

    def printList(self):
        if self.isEmpty():
            return print("List is empty")
        
        temp = self.last.next
        while(temp.next != self.last):
            print(temp.val, end="-->")
            temp = temp.next
        print(temp.val, end="-->")
        print(temp.next.val, end="-->")

    def printFor(self):
        temp = self.last
        for i in range(6):
            print(temp.val, end="-->")
            temp = temp.next


# cll = [81, 10, 44, 90, 32, 88, 63]
clst = circularLL()
clst.insertAtEmpty(23)
clst.insertAtlast(56)
clst.insertAtlast(81)
# clst.insertAtlast(42)
# clst.insertAtlast(45)
# clst.insertAtlast(99)
print(clst.isEmpty())
clst.printList()
clst.insert_at_first(14)
# clst.insert_after(56,78)
print()
clst.printList()
print()
clst.printFor()
