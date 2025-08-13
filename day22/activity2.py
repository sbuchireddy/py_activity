'''
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited amount is:", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Amount to be withdrawn:",amount)
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)
account.deposit(5500)
account.withdraw(500)
print("Current Balance:", account.get_balance())
'''
class BankAccount:

    def __init__(self, initial_balance=0):

        self.__balance = initial_balance  # private attribute
 
    def get_balance(self):

        return self.__balance
 
    def deposit(self, amount):

        if amount <= 0:

            print("Deposit amount must be positive.")

            return

        self.__balance += amount

        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
 
    def withdraw(self, amount):

        if amount <= 0:

            print("Withdrawal amount must be positive.")

            return

        if amount > self.__balance:

            print("Insufficient balance!")

            return

        self.__balance -= amount

        print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")
 
# Example usage:

acc = BankAccount(1000)

print("Initial balance:", acc.get_balance())
 
acc.deposit(500)

acc.withdraw(300)

acc.withdraw(1500)  # Should warn insufficient balance

acc.deposit(-50)    # Should warn invalid deposit
 
