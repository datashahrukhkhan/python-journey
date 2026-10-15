# Python Encapsulation and Abstraction

# aaj hum OOP ke last two major pillars detail mein seekhenge: Encapsulation aur Abstraction.

# Day 25 mein OOP ka overview, Day 26 mein classes and objects, aur Day 27 mein inheritance and polymorphism padha tha. Aaj hum samjhenge ki data ko protect kaise karte hain aur complex implementation ko hide karke simple interface kaise provide karte hain.



# Concept / Definition
# - Encapsulation: Data aur usse related methods ko ek class mein organize karna aur controlled access provide karna.
# - Abstraction: Unnecessary implementation details hide karke user ko sirf required functionality dikhana.
# Real-life example: ATM use karte waqt tum amount enter karke cash withdraw karte ho. Tumhe bank ke internal transaction system ka poora implementation jaanne ki zaroorat nahi hoti.


# Encapsulation — Data ko control karna
# Maan lo tum ek bank account bana rahe ho. Account ka balance koi bhi random value mein set kar de, toh problem ho sakti hai. Encapsulation se tum balance ko modify karne ke liye controlled methods provide kar sakte ho.




# Python mein access conventions
# Python mein Java jaisi strict public, protected, private access modifiers nahi hain. Common conventions ye hain:
# Syntax	                Meaning
# name	                    Public attribute; normally directly accessible
# _name	                    Non-public/protected-style convention; internal use ke liye intended
# __name	                Name mangling hoti hai; accidental access aur overriding conflicts kam karne mein help karti hai

# Important: _name aur __name absolute security barriers nahi hain. Python mein double underscore bhi data ko truly private ya inaccessible nahi banata.



# Public attribute
class Student:
    def __init__(self, name):
        self.name = name


student = Student("Shahrukh")

print(student.name)
student.name = "Aman"
print(student.name)

# Public attribute ko directly read aur update kiya ja sakta hai.


# Protected-style attribute
class Employee:
    def __init__(self, salary):
        self._salary = salary


employee = Employee(30000)

print(employee._salary)

# Python ise allow karta hai, lekin _salary convention indicate karta hai ki ise internal implementation detail samajhna chahiye.



# Double underscore
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())

# __balance ko class ke andar name-mangle kiya jaata hai. Isliye account.__balance normally AttributeError dega. Lekin ise strong security protection nahi samajhna chahiye.


# Practical Encapsulation — Bank Account
# Ab ek useful example dekhte hain jahan balance ko controlled methods se update kiya jaata hai.

class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return

        self.__balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount
        print("Withdrawal successful")

    def get_balance(self):
        return self.__balance


account = BankAccount("Shahrukh", 5000)

account.deposit(1000)
account.withdraw(500)

print("Balance:", account.get_balance())

# Is example mein encapsulation kaise help kar raha hai?
# - __balance internal attribute hai.
# - deposit() aur withdraw() balance update karne ke rules check karte hain.
# - get_balance() current balance read karne ka clear interface deta hai.
# - Negative ya invalid transactions reject ki jaati hain.
# Yaad rakho: actual financial systems mein sirf private attributes enough nahi hote. Database transactions, authorization, concurrency aur security checks bhi important hain.



# Abstraction — Internal complexity hide karna
# Socho tum car start karte ho. Tum key ya start button use karte ho; tumhe engine ke andar fuel injection, sensors aur ignition system ka exact process control nahi karna padta.
# Yahi abstraction ka basic idea hai: user ko simple interface do, implementation details ko hide rakho.
# Python mein abstraction ke liye abc module use kar sakte hain. Ismein:
# - ABC — abstract base class banane ke liye.
# - @abstractmethod — aisa method define karne ke liye jise concrete child classes ko implement karna hota hai.


# Abstract class

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)
print("Area:", rectangle.area())


# Samjho:
# 1. Shape ek abstract base class hai.
# 2. area() ek abstract method hai.
# 3. Rectangle apna area() implementation provide karta hai.
# 4. User simply rectangle.area() call karta hai; calculation method ke andar handle hoti hai.
# Agar tum Shape() directly create karne ki koshish karoge, Python TypeError raise karega. Isi tarah, required abstract method implement kiye bina Rectangle ka object create nahi kar sakte.


# Multiple implementations

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing card payment of ₹{amount}")


def checkout(payment_method, amount):
    payment_method.pay(amount)


checkout(UpiPayment(), 500)
checkout(CardPayment(), 1000)


# Encapsulation vs Abstraction
# Encapsulation	                                                                Abstraction
# Data aur related methods ko organize karta hai, controlled access ke saath	Unnecessary implementation details hide karta hai
# Focus: data aur access control	                                            Focus: simple interface
# Example: BankAccount ka balance methods se update karna	                    Example: Payment.pay() ka common interface
# Python mein naming conventions aur methods use hote hain	                    ABC aur @abstractmethod use kar sakte hain

# Memory trick:
# - Encapsulation = How do I control access to data?
# - Abstraction = What does the user need to know?















