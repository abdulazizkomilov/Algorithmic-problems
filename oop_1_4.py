class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Hisobingizdagi mablag': {self.balance} sum")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} summa qo'shildi. Yangi balans: {self.balance} sum")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} summa yechib olingan. Yangi balans: {self.balance} sum")
        else:
            print("Noto'g'ri amal, yetarli mablag' yo'q")

class ATM:
    @staticmethod
    def withdraw_from_account(account, amount):
        account.withdraw(amount)

# Test qismi
account = BankAccount("123456", 1000)
account.display_balance()

ATM.withdraw_from_account(account, 500)
account.display_balance()

account.deposit(200)
account.display_balance()


if __name__ == '__mian__':
    pass