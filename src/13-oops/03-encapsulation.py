# Encapsulation - wrappping data and methods together in one class
# It restricts direct access to the sensitive data.

class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount):
        
        print("="*20)
        print("!Deposit!")
        print("="*20)
        if amount < 0 or type(amount) != int:
            return "Invalid number"

        self.__balance += amount
        print(f"Amount deposited {self.__balance}")
        return self.__balance
    


    def withdraw(self, amount):
        print("="*20)
        print("Withdraw")
        print("="*20)
        if amount < 0 or type(amount) != int:
            return "Invalid number"
        
        self.__balance -= amount
        print(f"Amount withdrawn. Balance {self.__balance}")
        return self.__balance
    
    def get_balance(self):
        # a public method used to read private variable balance safely.
        return self.__balance


acc = BankAccount("John", 12345, 100)

print(acc.deposit(200))
print(acc.deposit(500))
print(acc.deposit(-500))

print(acc.withdraw(500))
print(acc.withdraw(1000))

print(acc.get_balance())




