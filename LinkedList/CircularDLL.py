class Node(object):
    def __init__(self,pre=None,val=None,next=None):
        self.pre = pre
        self.val = val
        self.next = next

class CircularDLL():
    def __init__(self):
        self.last = None

    def insertAtEmpty(self,val):
        if self.last !=None:
            return
        newNode = Node(val)
        self.last = newNode
        newNode.next = newNode
        newNode.pre = newNode

    def printList_asc(self):
        temp = self.last
        # while(temp.next != self.last):
        #     print(temp.val,end=" --> ")
        #     temp = temp.next
        print(temp.val,end=" --> ")

    def printFor(self):
        temp = self.last
        for i in range(3):
            print(temp.val,end=" --> ")
            temp = temp.next

cdll = CircularDLL()
cdll.insertAtEmpty(56)
cdll.printList_asc()
cdll.printFor()



        