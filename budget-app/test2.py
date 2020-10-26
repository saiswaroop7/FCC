def __init__(self, desc):
   self.ledger = {}
   self.ledger[desc] = desc
   self.funds = 0
   self.title = desc
   self.wd_info = {}
   
   
  
  def deposit(self, amount, *args):
    self.funds = self.funds + amount
    self.ledger[args[0]] = self.funds    
    return None

  def withdraw(self, amount, *args):
    if(self.check_funds(amount) > self.funds):
      return False
    else:
      self.funds = self.funds - amount
      if(len(args)==1):
       self.ledger[args[0]] = -(amount)
      else:
       self.ledger[""] = -(amount)
      return True

  def transfer(self, amount, acc):
    obj=acc.desc
    print(obj)
    a=self.withdraw(amount,f"Transfer to {obj}")
    b=obj.deposit(amount,f"Transfer from {self.name}")
    if(a==True):
        return True
    else:
        return False

    print(self.ledger)
    return None
  def get_balance(self):
    return self.funds

  def check_funds(self, amount):
    if(amount < self.funds):
      return False
    else:
      return True