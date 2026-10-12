# Python Object-Oriented Programming (OOP)
# aaj hum Python ka ek bahut important topic start kar rahe hain: Object-Oriented Programming (OOP). Iska use real-world applications ko organized, reusable aur maintainable banane ke liye hota h

# Tumhari Python journey mein ab tak hum functions, collections, modules, generators aur decorators padh chuke hain. Ab hum seekhenge ki data aur usse related functions ko ek saath kaise organize kiya jaata h


# Concept / Definition
# OOP is a programming approach that organizes code using classes and objects.


# Why do we need OOP?
# OOP ke bina bhi programs ban sakte hain. Lekin jaise-jaise project bada hota hai, data aur functions ko organize karna difficult ho sakta hai.
# OOP ke main benefits:
# - Reusability: Existing classes ko reuse kar sakte ho.
# - Organization: Related data aur behaviour ko ek saath rakh sakte ho.
# - Maintainability: Code ko update aur debug karna easier ho sakta hai.
# - Real-world modeling: Students, employees, bank accounts aur products jaise entities represent kar sakte ho.


# Class and Object
# Class kya hoti hai?
# Class ek blueprint hoti hai jo define karti hai ki objects ke paas kaunsa data aur behaviour hoga.
# Object kya hota hai?
# Object class ka ek instance hota hai. Ek class se multiple objects bana sakte hain.

# Example:-
class Student:
    pass


student1 = Student()
student2 = Student()

print(type(student1))
print(type(student2))

# class Student: — class define karta hai.
# pass — temporarily empty class body allow karta hai.
# student1 aur student2 — do alag objects hain.

print("\n")
# Attributes and Methods
# OOP mein do important terms hain:
# - Attributes: Object ka data, jaise name aur age.
# - Methods: Class ke andar defined functions, jaise introduce().

class Student:
    def introduce(self):
        print("Hello, I am a student.")


student1 = Student()
student1.introduce()

# Yahan introduce() ek method hai. self current object ko refer karta h.

print("\n")

# __init__() and self
# Ab class ko useful banate hain, taaki har student ka apna data ho.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")


student1 = Student("Aman", 20)
student2 = Student("Shahrukh", 22)

student1.introduce()
print()
student2.introduce()



# Is example mein:-
# - __init__() object create hote waqt initialize karne ke liye use hota hai.
# - self.name object ka attribute hai.
# - self.age object ka attribute hai.
# - Student("Aman", 20) ek object create karta hai.

# Memory trick: Class = blueprint, Object = actual item, Attribute = data, Method = action.


# The four pillars of OOP
# OOP ke four commonly taught pillars hain. Aaj inka overview samjho; inhe detail mein agle lessons mein padhenge.






