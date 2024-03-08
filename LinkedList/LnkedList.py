class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkdList(object):
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        if self.head == None:
            return True
    
    def insert_at_last(self,val):
        newNode = Node(val)

        if self.isEmpty():
            self.head = newNode
            return
            
        temp = self.head
        while(temp.next!= None):
            temp = temp.next
        temp.next = newNode
        
    def insert_at_first(self,val):
        newNode = Node(val)

        if self.isEmpty():
            self.head = newNode
            return
        
        temp = self.head

        self.head = newNode
        newNode.next = temp

    def insert_after(self,element,data):
        newNode = Node(data)

        if self.isEmpty():
            return
        
        temp = self.head

        if temp.next == None:
            if temp.val == element:
                temp.next = newNode
                return
        
        while(temp.next !=None):
            if(temp.val == element):
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next

        if temp.val == element:
            temp.next = newNode
            return

    
    def delete_last(self):
        temp = self.head
        while(temp.next.next!=None):
            temp = temp.next
        temp.next = None
            
        
    def printList(self):
        temp = self.head
        while(temp.next !=None):
            print(temp.val,end="-->")
            temp = temp.next
        print(temp.val,end="-->")
                   
    

    def delete_data(self,data):
        if(self.isEmpty()):
            return 
        
        temp = self.head
        
        while(temp.next != None):
            if(temp.next.val == data):
                break
            temp = temp.next
        temp.next = temp.next.next

    
    
    def search(self,data):
        temp = self.head
        while(temp.next !=None):
            if(temp.val == data):
                return data
            temp = temp.next

        if(temp.val == data):
            return data

    def delete_first(self):
        if self.isEmpty():
            return None
        
        self.head = self.head.next 

    def ascending_sort(self):
        c = self.count()
        while(c>0):
            temp = self.head
            while(temp.next != None):
                if(temp.val > temp.next.val):
                    temp.val,temp.next.val = temp.next.val,temp.val 
                temp = temp.next
            c-=1

    
    def descending_sort(self):
        c = self.count()
        while(c>0):
            temp = self.head
            while(temp.next != None):
                if(temp.val < temp.next.val):
                    temp.val,temp.next.val = temp.next.val,temp.val 
                temp = temp.next
            c-=1

    def count(self):
        temp = self.head
        count = 0
        while(temp.next !=None):
            count+=1
            temp = temp.next
        return count


        


# ll = [650,10,44,90,32,88,63]
               
lst = LinkdList()
lst.head = Node(1)

# for i in ll:
#     lst.insert_at_last(i)

lst.insert_at_last(32)
lst.insert_at_last(63)
lst.insert_at_last(44)
lst.insert_at_first(90)
lst.insert_at_first(10)
lst.delete_data(32)

lst.insert_at_first(650)
lst.insert_after(650,88)
lst.delete_first()

lst.printList()
print()
lst.ascending_sort()
lst.printList()
print()
lst.descending_sort()
lst.printList()
print(lst.search(4))



           

    

