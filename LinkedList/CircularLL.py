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

    def insertAtEmpty(self,val):
        if self.last != None:
            return None 
        
        newNode = Node(val)
        newNode.next = newNode
        self.last = newNode


    def insert_at_first(self,val):
        if self.isEmpty():
            return self.insertAtEmpty(val)
        

        newNode = Node(val)
        newNode.next = self.last.next
        self.last.next = newNode

    def insert_at_last(self,val):
        if self.isEmpty():
            return self.insertAtEmpty(val)
        
        newNode = Node(val)
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

    def insert_after(self,elem,val):
        if self.isEmpty():
            return None
        
        newNode = Node(val)
        temp = self.last.next
        if self.last.val == elem:
            return self.insert_at_last(val)
        
        while(temp !=self.last):
            if(temp.val == elem):
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next

        

    def delete_first(self):
        if not self.isEmpty():
            if self.last.next == self.last:
                self.last = None    
            else:
                self.last.next = self.last.next.next
            
    def delete_last(self):
        if not self.isEmpty():
            if self.last.next == self.last:
                self.last = None

            else:
                temp = self.last
                while(temp.next != self.last):
                    temp = temp.next

                temp.next = self.last.next
                self.last = temp

    def delete_data(self,elem):
        if not self.isEmpty():
            if self.last.next == self.last and self.last.val == elem:
                self.last = None
            
            else:
                temp = self.last
                if temp.val==elem:
                    self.delete_last()

                else:
                    while(temp.next != self.last):
                        if temp.next.val == elem:
                            temp.next = temp.next.next
                            break
                        temp = temp.next


    def printList(self):
        if self.isEmpty():
            return print("List is empty")
        
        temp = self.last.next
        while(temp != self.last):
            print(temp.val, end="-->")
            temp = temp.next
        print(temp.val, end="-->")

    def printFor(self):
        temp = self.last.next
        for i in range(10):
            print(temp.val, end="-->")
            temp = temp.next


# cll = [81, 10, 44, 90, 32, 88, 63]
clst = circularLL()
clst.insert_at_last(81)
clst.insert_at_last(42)
clst.insert_at_last(45)
clst.insert_at_last(99)
print(clst.isEmpty())

clst.insert_at_first(14)
clst.insert_at_first(28)
clst.insert_at_last(56)
clst.printList()
clst.insert_after(99,78)
print()
clst.printList()
clst.delete_first()
# clst.delete_last()
# clst.delete_last()
# clst.delete_data(81)

print()
clst.printList()
print()
clst.printFor()
