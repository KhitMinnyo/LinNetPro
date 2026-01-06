### KMN Banking System V1

# Logic 
#1. The Core
### Attributes: owner name, account number, balance, ..
### Methods:    Cash in, Cash Out, ....

#2. Sepcialization
### Saving Accounts (need to get interest)
### Checking Accounts (need Overdraft)

#3. Management
### Create Account
### Store Account (Dictionary)
### Transfer process

#4. Persistence
### File I/O
### Run ==> save data (function)
### rerun ==> load data (function)

#5. Traceability 
### Transaction Logs
### Each transaction (own diary) (list)

#6. Polishing
### try-except (prevention erros)

import json
import random 

# Base Class
class Account:
    def __init__(self, holder, balance=0, acc_num=None):
        self.holder = holder 
        self.acc_num = acc_num if acc_num else str(random.randint(100000, 999999)) 
        self._balance = balance ## Protected Attribute 

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount cannot be zero.")
        self._balance += amount 
        return True
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("You have no enough money to withdraw.")
        self._balance -= amount 
        return True
    
    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"[{self.acc_num}] {self.holder} | Balance: {self._balance:.2f}"
    
# Saving Account 
class SavingAccount(Account):
    def apply_interest(self):
        interest = self._balance * 0.02 
        self._balance += interest 
        print(f"Total interest {interest:.2f} were added.")

# Checking Account
class CheckingAccount(Account):
    def withdraw(self, amount):
        limit = 1000000 #Overdraft limit
        if amount > (self._balance + limit):
            raise ValueError("Withdraw amount exceeds than Maximum amount.")
        self._balance -= amount
        return True
    
# Main Bank Features
#Main system
class BankSystem:
    def __init__(self, filename="bank_data.json"):
        self.accounts = {}
        self.filename = filename 
        self.load_data()

    def create_account(self, name, acc_type, initial_dep):
        if acc_type == "1":
            acc = SavingAccount(name, initial_dep)
        else:
            acc = CheckingAccount(name, initial_dep)

        self.accounts[acc.acc_num] = acc 
        self.save_data()
        print(f"Your account was created. Your account number: {acc.acc_num}")

    def save_data(self):
        data = {}
        for acc_num, acc in self.accounts.items():
            data[acc_num] = {
                "holder": acc.holder,
                "balance": acc.get_balance(),
                "type": "Saving" if isinstance(acc, SavingAccount) else "Checking"
            }
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for acc_num, info in data.items():
                    if info["type"] == "Saving":
                        acc = SavingAccount(info["holder"], info["balance"], acc_num)
                    else:
                        acc = CheckingAccount(info["holder"], info["balance"], acc_num)
                    self.accounts[acc_num] = acc 

        except FileNotFoundError:
            pass

# Main Menu

bank = BankSystem()
while True:
    print("\n--- KMN Bank System ---")
    print("1. Create Account | 2. Deposit/Withdraw | 3. Checking | 4. Exit")
    choice = input("Enter 1 to 4 : ")

    try:
        if choice == "1":
            name = input("Enter full name: ")
            a_type = input("(1. Saving | 2. Checking) Account type: ")
            dep = float(input("Initial Deposit Amount: "))
            bank.create_account(name, a_type, dep)

        elif choice == "2":
            num = input("Enter account number: ")
            if num in bank.accounts:
                amt = float(input("Enter deposite amount: "))
                action = input("1. Deposit | 2. Withdraw : ")
                if action == "1":
                    bank.accounts[num].deposit(amt)
                else:
                    bank.accounts[num].withdraw(amt)
                bank.save_data()
                print("Your activity was successful.")
            else: 
                print("Account not found. Please, check your account number.")

        elif choice == "3":
            for acc in bank.accounts.values():
                print(acc)

        elif choice == "4":
            break

    except Exception as e:
        print(f"Error: {e}")


