class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balace = balance

    def deposit(self, amount):
        self.balace += amount
        print(f"Hisobingizga {amount} summa qo'shildi. Jami balance {self.balace} sum")

    def withdraw(self, amount):
        if amount <= self.balace:
            self.balace -= amount
            print(f"Hisobingizdan {amount} pul yichib olindi. Jami balance {self.balace} sum")

        else:
            print("Noto'g'ri amal, yetarli mablag' yo'q.")
    
class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balace * (self.interest_rate / 100)
        self.balace += interest_amount
        print(f"Foiz qo'shildi. Yangi balance: {self.balace} sum")

a1 = Account(12345, 1000)
saving_account = SavingAccount(54321, 5000, 5)

a1.deposit(200)
a1.withdraw(50)

saving_account.deposit(1000)
saving_account.add_interest()

if __name__ == '__main__':
    pass