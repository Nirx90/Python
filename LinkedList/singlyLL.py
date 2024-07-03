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

sl.printLL()


