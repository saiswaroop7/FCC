class Category:
    def __init__(self, desc):
        self.ledger = [{} for _ in range(6)]
        self.funds = 0.0
        self.ledcount = 0
        self.title = desc
        self.expense = 0

    def deposit(self, amount, *args):
        amount = format(amount, '.2f')
        self.funds = self.funds + float(amount)

        if (len(args) == 1):
            self.ledger[self.ledcount] = {
                "amount": self.funds,
                "description": args[0]
            }
            self.ledcount = self.ledcount + 1
        else:
            self.ledger[self.ledcount] = {
                "amount": self.funds,
                "description": ""
            }
            self.ledcount = self.ledcount + 1

        return None

    def withdraw(self, amount, *args):
        if (self.check_funds(amount) == True):
            self.funds = self.funds - round(float(amount), 2)
            if (len(args) == 1):
                self.ledger[self.ledcount] = {
                    "amount": -round(float(amount), 2),
                    "description": args[0]
                }
                self.ledcount = self.ledcount + 1
                self.expense = self.expense + amount
            else:
                self.ledger[self.ledcount] = {
                    "amount": -round(float(amount), 2),
                    "description": ""
                }
                self.ledcount = self.ledcount + 1
                self.expense = self.expense + amount
            return True
        else:
            return False

    def transfer(self, amount, acc):
        if (self.check_funds(amount) == True):
            self.funds = self.funds - round(float(amount), 2)
            self.ledger[self.ledcount] = {
                "amount": -round(float(amount), 2),
                "description": "Transfer to " + acc.title.capitalize()
            }
            self.expense = self.expense + amount
            self.ledcount = self.ledcount + 1
            acc.ledger[acc.ledcount] = {
                "amount": round(float(amount), 2),
                "description": "Transfer from " + self.title
            }
            acc.ledcount = acc.ledcount + 1
            acc.funds = acc.funds + round(float(amount), 2)
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def check_funds(self, amount):
        if (self.funds >= amount):
            return True
        else:
            return False

    def __str__(self):
        pad = int((30 - len(self.title)) / 2)
        res = pad * '*' + self.title + '*' * pad + "\n"
        print(res)
        main = res
        for i in self.ledger:
            if (i == {}):
                break
            pad2 = len(i["description"][0:29 - len(str(i["amount"]))])
            c = 0
            if (len(str(i["amount"])) == 5):
                tmps = str(i["amount"])
                if (tmps[0] == "-"):
                    c = c + 1
            main = main + str(
                i["description"][0:29 - c - len(str(i["amount"]))]) + str(
                    format(i["amount"], '.2f')).rjust(30 - pad2 + c) + "\n"
            """print(
              str(i["description"][0:29 - c - len(str(i["amount"]))]) +
              str(format(i["amount"], '.2f')).rjust(30 - pad2 + c) , ' ')"""

        #print("Total: " + str(format(self.funds, '.2f')))
        main = main + str("Total: " + str(format(self.funds, '.2f')))
        return main


def create_spend_chart(categories):

    res = 'Percentage spent by category\n'
    withdraws = sum(i.expense for i in categories)
    percentages = len(categories) * [0.0]
    c = 0
    for i in categories:
      percentages[c] = (round((i.expense / withdraws) * 100, 2))
      c = c + 1
    for i in range(100, -10, -10):
        res = res + str(i).rjust(3, " ") + '|'
        for j in percentages:
            if j >= i:
                res = res + ' o '
            else:
                res = res + '   '
        res = res + ' \n'
    res = res + '    ' + '-' * len(percentages) * 3 + '-\n'
    fill = max(len(i.title) for i in categories)
    for i in range(fill):
        res = res + '    '
        for j in categories:
            if i < len(j.title):
                res = res + ' ' + j.title[i] + ' '
            else:
                res = res + '   '
        res = res + ' \n'
    return res.rstrip() + '  '
