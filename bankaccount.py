class BankAccount:
    def __init__(self):
        self.balance = 0 

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Error: Insufficient funds!")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


Joe = BankAccount()
John = BankAccount()

Joe.balance = 5000
John.balance = 3000

print("Account 1:")
Joe.display_balance()
Joe.deposit(2000)
Joe.withdraw(1500)
Joe.display_balance()

print("\n")

print("Account 2:")
John.display_balance()
John.deposit(1000)
John.withdraw(5000)
John.withdraw(2000)
John.display_balance()