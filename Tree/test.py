class Node(object):
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        temp = self.root
        if temp is None:
            self.root = Node(data)
            return
        
        while(temp is not None):
            if data < temp.val:
                ref = temp
                temp = temp.left
            else:
                ref = temp
                temp = temp.right

        if data < ref.val:
            ref.left = Node(data)
        elif data > ref.val:
            ref.right = Node(data)

    def search(self,element):
        temp = self.root
        while(temp is not None):
            if temp.val == element:
                return temp.val
            if element < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def preOrder(self):
        self.callpreOrder(self.root)

    def InOrder(self):
        self.callInOrder(self.root)

    def postOrder(self):
        self.callpostOrder(self.root)

    def callpreOrder(self,temp):
        print(temp.val,end=" ")
        if temp.left is not None:
            self.callpreOrder(temp.left)
        if temp.right is not None:
            self.callpreOrder(temp.right)

    def callpostOrder(self,temp):
        if temp.left is not None:
            self.callpostOrder(temp.left)
        if temp.right is not None:
            self.callpostOrder(temp.right)
        print(temp.val,end=" ")

    def callInOrder(self,temp):
        if temp.left is not None:
            self.callInOrder(temp.left)
        print(temp.val,end=" ")
        if temp.right is not None:
            self.callInOrder(temp.right)
        

bt = BST()

bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(17)
bt.insert(1)
bt.insert(9)
bt.insert(14)

bt.preOrder()
print()
bt.postOrder()
print()
bt.InOrder()
print()
print(bt.search(16))
