class Node(object):
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.callInsert(self.root,data)

    def callInsert(self,temp,data):
        if self.root is None:
            self.root = Node(data)
            return 
        if data < temp.val:
            if temp.left is not None:
                self.callInsert(temp.left,data)
            else:
                temp.left = Node(data)

        if data > temp.val:
            if temp.right is not None:
                self.callInsert(temp.right,data)
            else:
                temp.right = Node(data)

    def search(self,elem):
        return self.callSearch(self.root,elem)

    def callSearch(self,temp,elem):
        if temp:
            if temp.val == elem:
                return temp.val
            if elem < temp.val:
                return self.callSearch(temp.left,elem)
            if elem > temp.val:
                return self.callSearch(temp.right,elem)
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
print(bt.search(14))
