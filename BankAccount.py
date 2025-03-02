class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{self.name} deposited ${amount:.2f}. {self.name}'s new balance: ${self.balance:.2f}")
        else:
            print("deposit amount must be greater than zero.")
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"{self.name} withdrew ${amount:.2f}. {self.name}'s new balance: ${self.balance:.2f}")
        elif amount>self.balance:
            print("withdrawal amount is greater than balance.")
        else:
            print("withdrawal amount must be greater than zero.")
    def get_balance(self):
        print(f"{self.name}'s balance: ${self.balance:.2f}")
        return self.balance

account=BankAccount("jasper",0)
account.get_balance()
account.deposit(250)
account.withdraw(250)