class Box(object):
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class singlyLL(object):

    def __init__(self):
        self.head = None

    def isEpmpty(self):
        if self.head == None:
            return True

    def insert_at_first(self,value):
        newBox = Box(value,self.head)
        self.head = newBox

    def insert_at_last(self,value):
        if self.isEpmpty():
            return self.insert_at_first(value)
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Box(value)

    def printLL(self):
        if self.isEpmpty():
            return
        temp = self.head
        while temp:
            print(temp.value,end="-->")
            temp = temp.next

sl = singlyLL()
list1 = [4,6,8,12,33,23]

for i in list1:
    sl.insert_at_first(i)

sl.insert_at_last(25)
sl.printLL()


