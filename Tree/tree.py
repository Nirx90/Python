class Node():
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

    def preOrder(self):
        print(self.val,end=" ")
        if self.left:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()

    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:
            self.right.postOrder()
        print(self.val,end = " ")

    def InOrder(self):
        if self.left is not None:
            self.left.InOrder()
        print(self.val,end = " ")
        if self.right is not None:
            self.right.InOrder()




root  = Node(50)

root.left = Node(51)
root.left.right = Node(30)
root.left.right.left = Node(34)
root.left.right.left.right = Node(42)
root.left.right.right = Node(31)
root.left.right.right.right = Node(71)
root.left.right.right.right.left = Node(33)
root.left.right.right.right.right = Node(1)
root.left.left = Node(44)
root.left.left.right = Node(41)
root.left.left.left = Node(40)
root.left.left.left.left = Node(36)

root.right = Node(2)
root.right.right = Node(3)
root.right.right.left = Node(8)
root.right.right.right = Node(5)
root.right.right.right.left = Node(7)
root.right.right.right.left.right = Node(12)
# root.left.left = Node(4)
# root.left.right = Node(5)

# root.right.right = Node(7)
# root.right.left = Node(6)

root.preOrder()
print()
root.postOrder()
print()
root.InOrder()

    
