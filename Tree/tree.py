class Node(object):
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,temp,data):
        if self.root is None:
            self.root = Node(data)
            return 
        if data < temp.val:
            if temp.left is not None:
                self.insert(temp.left,data)
            else:
                temp.left = Node(data)

        if data > temp.val:
            if temp.right is not None:
                self.insert(temp.right,data)
            else:
                temp.right = Node(data)


    def preOrder(self,temp):
        print(temp.val,end=" ")
        if temp.left is not None:
            self.preOrder(temp.left)
        if temp.right is not None:
            self.preOrder(temp.right)

    def postOrder(self,temp):
        if temp.left is not None:
            self.postOrder(temp.left)
        if temp.right is not None:
            self.postOrder(temp.right)
        print(temp.val,end=" ")

    def InOrder(self,temp):
        if temp.left is not None:
            self.InOrder(temp.left)
        print(temp.val,end=" ")
        if temp.right is not None:
            self.InOrder(temp.right)
        

bt = BST()
bt.insert()
bt.root = Node(10)
root = bt.root
bt.insert(root,5)
bt.insert(root,15)
bt.insert(root,3)
bt.insert(root,7)
bt.insert(root,12)
bt.insert(root,17)
bt.insert(root,1)
bt.insert(root,9)
bt.insert(root,14)


# bt.preOrder(root)
# print()
# bt.postOrder(bt.root)
# print()
bt.InOrder(root)
