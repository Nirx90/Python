class Base():
    def __init__(self):
        print("Base constructor")
        
class derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived constructor")
        
d = derived()