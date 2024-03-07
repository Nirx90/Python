class Node(object):
    def __init__(self,val=None,pre=None,next=None):
        self.pre = pre
        self.val = val
        self.next = next

class CircularDLL(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        
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

        if temp.next == self.head:
            newNode.next = temp
            newNode.pre = temp
            temp.next = newNode
            temp.pre = newNode

        else:
            newNode.next = temp
            newNode.pre = temp.pre
            temp.pre.next = newNode
            temp.pre = newNode


    def insert_at_first(self,val):
        if self.head == None:
            return self.insertAtEmpty(val)
        
        newNode = Node(val) 
        temp = self.head
        
        if temp.next == self.head:
            newNode.next = temp
            newNode.pre = temp
            temp.next = newNode
            temp.pre = newNode
            self.head = newNode

        else:       
            newNode.pre = temp.pre
            temp.pre.next = newNode
            newNode.next = temp
            temp.pre = newNode
            self.head = newNode


        
    def insert_after(self,elem,data):
        if self.isEmpty():
            return
        
        temp = self.head
        newNode = Node(data)
        if temp.val == elem:
            newNode.pre = temp
            newNode.next = temp.next
            temp.next.pre = newNode
            temp.next = newNode
            return
        
        while(temp.next != self.head):
            if temp.val == elem:
                break
            temp = temp.next


        if temp.next == self.head:
            if temp.val == elem:
                return self.insert_at_last(data)
            else:
                return 
            

        newNode.next = temp.next
        temp.next.pre = newNode
        temp.next = newNode
        newNode.pre = temp

    def delete_first(self):
        if self.isEmpty():
            return
        
        temp = self.head
        temp.pre.next = temp.next
        temp.next.pre = temp.pre
        self.head = temp.next

    def delete_last(self):
        if self.isEmpty():
            return
        
        temp = self.head
        temp.pre = temp.pre.pre
        temp.pre.next = temp

    def deleteItem(self,item):
        if self.isEmpty():
            return
        
        temp = self.head
        while(temp.next != self.head):
            if temp.val == item:
                break
            temp = temp.next

        
        

    def search(self,data):
        if self.isEmpty():
            return
        
        temp = self.head

        if temp == None:
            return None
        
        elif temp.val == data:
            print(temp.val,"founded")
            return temp.val
        
        else:
            while(temp.next != self.head):
                if temp.val == data:
                    print(temp.val,"founded")
                    return temp.val
                temp = temp.next

            if temp.next == self.head:
                temp.val == data
                print(temp.val," Founded")
                return temp.val
            
            return None
            
    def printList_asc(self):
        if self.isEmpty():
            return
        
        temp = self.head
        while(temp.next != self.head):
            print(temp.val,end=" --> ")
            temp = temp.next
        print(temp.val,end=" --> ")

    def printList_desc(self):
        if self.isEmpty():
            return
        
        temp = self.head.pre
        while(temp.pre != self.head):
            print(temp.val,end=" --> ")
            temp = temp.pre
        print(temp.val,end=" --> ")
        print(temp.pre.val,end=" --> ")

    def printFor(self):
        if self.isEmpty():
            return
        
        temp = self.head
        for i in range(15):
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
cdll.insert_at_first(128)
cdll.printList_asc()

print()
cdll.printList_asc()
print()
cdll.delete_first()
cdll.delete_last()
cdll.insert_at_last(34)
# cdll.delete_last()
cdll.insert_after(26,111)
cdll.printList_asc()


print()
cdll.printFor()

print()

cdll.printList_desc()
print()

# cdll.search(13)