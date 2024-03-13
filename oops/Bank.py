class Bank:
    bname = 'BOB'
    def __init__(self, name):
        self.name = name
        self.accBal = 1000
    def withdraw(self, withamt):
        if self.accBal >= withamt:
            self.accBal -= withamt
            print(f"Withdrawal successful.Updated balance: {self.accBal}/- ₹")
        else:
            print('Insufficient Balance')
    def deposit(self, depoamt):
        self.accBal += depoamt
        print(f"Deposit successful.Updated balance: {self.accBal}/- ₹")
    def show(self):
        print(f"{self.bname} your acc balance is {self.accBal}")
objList = []
for i in range(5):
    objList[i].append

