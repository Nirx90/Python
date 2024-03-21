class Base1():
    def __init__(self):
        print("parent1 classs")
        
class Base2():
    def __init__(self):
        # super().__init__()
        print("Parent2 classs")
        
class child(Base2,Base1):
    def __init__(self):

        super().__init__()
        Base1()
        print("child  classs")
        
c2 = child()