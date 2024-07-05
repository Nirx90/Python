class Dequeu:
    arr = []
    def first_in(self,n):
        Dequeu.arr.insert(0,n)
        print(f"first_in {n} {Dequeu.arr}")
    
    def first_out(self):
        Dequeu.arr.pop(0)
        print(f"first_out {Dequeu.arr}")

    def last_in(self,n):
        Dequeu.arr.append(n)
        print(f"last_in {n} {Dequeu.arr}")

    def last_out(self):
        Dequeu.arr.pop()
        print(f"first_in {Dequeu.arr}")

    def print(self):
        return Dequeu.arr


dq = Dequeu()
dq.first_in(5)
dq.first_in(8)
dq.last_in(10)
dq.first_out()

  
