class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(200) 

print("Final Balance:", account.get_balance())