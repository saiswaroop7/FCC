def __init__(self,name):
    self.name=name
    self.ledger=list()
def check_funds(self,amount):
    fund=0
    n=len(self.ledger)
    for i in range(n):
        fund=fund+self.ledger[i]["amount"]
    if fund<amount:
        return False
    else:
        return True
def deposit(self,amount,description=""):
    #initialising a dictionary
    self.dep=dict()
    #adding the amount and description to dictionary
    self.dep["amount"]=amount
    self.dep["description"]=description
    #adding the deposit to ledger list
    self.ledger.append(self.dep)

def withdraw(self,amount,description=""):
    #checking if total amount less than or greaten than amount to be withdrawn
    l=self.check_funds(amount)

    if(l==True):
        self.withd=dict()
        self.withd["amount"]=-(amount)
        self.withd["description"]=description
        self.ledger.append(self.withd)
        return True
    else:
        return False
def get_balance(self):
    fund=0
    n=len(food.ledger)
    #retrieving the total fund in ledger
    for i in range(n):
        fund=fund+food.ledger[i]["amount"]
    return fund
def transfer(self,amount,obname):
    objectname=obname.name
    a=self.withdraw(amount,f"Transfer to {objectname}")
    b=obname.deposit(amount,f"Transfer from {self.name}")
    if(a==True):
        return True
    else:
        return False
def check_funds(self,amount):
    fund=0
    n=len(self.ledger)
    for i in range(n):
        fund=fund+self.ledger[i]["amount"]
    if fund<amount:
        return False
    else:
        return True