class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            
    def display_balance(self):
        print(f"Account Number: {self.account_number}\nCurrent Balance: ${self.balance:.2f}")
        
my_account = BankAccount("123456789")
my_account.deposit(1000)
my_account.withdraw(500)
my_account.display_balance()