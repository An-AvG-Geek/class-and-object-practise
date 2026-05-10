# account_holder
# balance

class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self,account_holder,balance):
        self.account_houlder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print(f"insufficient balance")

    def show_balance(self):
        print(f"the remaining balance is {self.balance}")

    @classmethod
    def change_bank(cls,newname):
        cls.bank_name=newname

    @staticmethod
    def is_valid_amount(amount):
        if amount>0:
            return True
        else:
            return False
        

if BankAccount.is_valid_amount(500):
    user1=BankAccount("felix",500)
    user1.show_balance()
    user1.deposit(1000)
    user1.show_balance()
    user1.withdraw(5000)
    user1.withdraw(200)
    user1.show_balance()
    BankAccount.change_bank("yes bank")
    print(f"{BankAccount.bank_name}")


