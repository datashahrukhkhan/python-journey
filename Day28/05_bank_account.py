class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a positive amount")
            return

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a positive amount")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Shahrukh", 5000)
account.deposit(1000)
account.withdraw(500)

print(account.get_balance())