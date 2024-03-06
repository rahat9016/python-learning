class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\n Account {self.name} created.\n Balance = {self.balance:.2f}")

    def getBalance(self):
        print(f"\n Account '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposit completed. \n Account '{self.name}' Balance = ${self.balance:.2f}")
        self.getBalance()
    
    def visibleTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        try:
            self.visibleTransaction(amount)
            self.balance = self.balance - amount
            print(f"\n Withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n********\n\nBeginning Transfer...")
            self.visibleTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"Transfer complete! \n\n********")
        except BalanceException as error:
            print(f"\n Transfer interrupted: {error}")