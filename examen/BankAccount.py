class BankAccount:
    def __init__(self, account_number : str, balance : float, daily_limit = 1000.0):
        assert account_number[:2]== "BE" or account_number[:2]=="NL", "Fout Account Number!"
        self.account_number = account_number
        self.balance = balance
        self.daily_limit = daily_limit
        self.amount_withdrawn_today = 0.0

    def deposit(self, amount: float):
        assert amount > 0.0, "Amount moet groter dan 0!"
        self.balance += amount

    def withdraw(self,amount: float):
        if amount <= 0:                                      #controles die gevraagd waren uitvoeren
            print("Amount moet groter dan 0!")
            return False

        if self.amount_withdrawn_today >= self.daily_limit:
            print("U hebt vandaag uw limiet bereikt!")
            return False

        if amount > self.balance:
            print("Niet genoeg op uw rekening!")
            return False

        self.balance -= amount                              #indien tests slagen
        self.amount_withdrawn_today += amount
        return True

    def reset_daily_limit(self):
        self.amount_withdrawn_today = 0.0

    def __str__(self):
        return f"{self.account_number} {self.balance:.2f} {self.daily_limit}"











