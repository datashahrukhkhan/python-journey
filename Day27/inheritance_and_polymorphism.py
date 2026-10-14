# aaj hum OOP ke do important concepts seekhenge: Inheritance aur Polymorphism.

# Kal humne classes, objects, attributes aur methods padhe the. Aaj unhi concepts ka use karke code reuse karna aur same method se different behaviour achieve karna seekhenge.


# Concept / Definition
# Inheritance: Ek class doosri class ke attributes aur methods ko inherit kar sakti hai.
# Polymorphism: Same interface ya method different objects ke liye different behaviour provide kar sakta hai.
# Simple Hinglish example:
# - Inheritance: Car aur Bike, dono Vehicle se common properties le sakte hain.
# - Polymorphism: Car aur Bike dono ka move() method ho sakta hai, lekin unka behaviour different ho sakta hai.



# Inheritance — Code reuse karna
# Maan lo tumhare paas Animal class hai. Usmein eat() method hai. Ab Dog aur Cat classes ko bhi eat karna hai.
# Har class mein same method dobara likhne ke bajaye, inheritance use kar sakte ho.

# Basic inheritance
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()

# Samjho:-
# - Animal — parent class, jise base class bhi kehte hain.
# - Dog(Animal) — child class, jo Animal se inherit karti hai.
# - dog.eat() — parent class ka inherited method call karta hai.
# - dog.bark() — child class ka apna method call karta hai.
# Memory trick: Parent gives common features; child can reuse and extend them.


# Inheritance ke types
# Python mein inheritance ke commonly taught types ye hain:

# 1. Single inheritance
# Ek child class, ek parent class se inherit karti hai.
class Dog(Animal):
    pass

# 2. Multiple inheritance
# Ek child class, multiple parent classes se inherit karti hai.
# class Child(Father, Mother):
#     pass

# 3. Multilevel inheritance
# Ek class doosri se aur teesri usse inherit karti hai.
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# 4. Hierarchical inheritance
# Multiple child classes ek hi parent se inherit karti hain.
class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 5. Hybrid inheritance
# Do ya zyada inheritance patterns ka combination.
# Python multiple inheritance support karta hai; complex hierarchies mein method resolution order (MRO) important hota hai.



# super() — Parent class ka method use karna
# super() child class se parent class ke methods ko call karne mein help karta hai.
class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("Name:", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_info(self):
        super().show_info()
        print("Breed:", self.breed)


dog = Dog("Bruno", "Labrador")
dog.show_info()


# Yahan super().__init__(name) parent ka initializer call karta hai, aur super().show_info() parent ka method call karta hai.


# Method overriding
# Jab child class parent class ke existing method ko apne implementation se redefine karti hai, use method overriding kehte hain.
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()

# Dog ke object par sound() call karne se child class ka version execute hota hai.



# Polymorphism — Same interface, different behaviour
# Poly = many, morph = forms.
# Polymorphism ka matlab hai ki same method name ya interface different objects ke liye different behaviour de sakta hai.
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()




# Inheritance vs Polymorphism

# Inheritance	                                        Polymorphism
# Existing class ka behaviour reuse karna	            Same interface se different behaviour
# Parent-child relationship important ho sakta hai	    Different objects ka common interface ho sakta hai
# Example: Dog(Animal)	                                Example: Dog.sound() aur Cat.sound()
# Focus: reuse and extension	                        Focus: flexibility

# Yaad rakhna: Inheritance aur polymorphism related hain, lekin same concept nahi hain. Polymorphism inheritance ke bina bhi duck typing se achieve ho sakta hai.





