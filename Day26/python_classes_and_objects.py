# Python Classes and Objects


# aaj hum OOP ko practically strong karenge. Kal tumne OOP ka overview padha tha; aaj focus rahega classes, objects, constructors, instance attributes, class attributes aur methods par.


# Concept / Definition
# - Class: Blueprint jo define karti hai ki objects ka data aur behaviour kya hoga.
# - Object: Class ka instance.
# - Attribute: Object ya class se associated data.
# - Method: Class ke andar defined function.
# - Constructor/Initializer: Object create hone par initial values set karne ke liye __init__() use hota hai. Technically, __new__() object create karta hai aur __init__() usse initialize karta hai.
# Real-life example: Ek Mobile class mein brand, model aur price ho sakte hain. Samsung aur Apple ke phones us class ke alag objects ho sakte hain.



# Basic class and object

from attr import attributes


class Student:
    pass


student1 = Student()
student2 = Student()

print(type(student1))
print(type(student2))

# Yahan Student class hai aur student1, student2 uske objects hain.
# pass ka matlab hai ki abhi class ke andar koi implementation nahi likhi gayi hai.


print("\n")

# __init__() and self
# Ab objects ko apna data denge.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Aman", 20)
student2 = Student("Shahrukh", 22)

student1.display_info()
print()
student2.display_info()




# Samjho:-
# - __init__() — object ko initialize karta hai.
# - self — current object ko refer karta hai.
# - self.name = name — object ke andar name attribute store karta hai.
# - Student("Aman", 20) — naya Student object initialize karta hai.
# Memory trick: self.name object ka data hai; name constructor ko mila parameter hai.







# Instance attributes vs Class attributes
# Ye Day 26 ka important concept hai.
# Instance attribute
# Har object ki apni value hoti hai.

# Class attribute
# Class se associated shared value hoti hai, jise instances bhi access kar sakte hain.



class Student:
    university = "JECRC University"

    def __init__(self, name):
        self.name = name


student1 = Student("Aman")
student2 = Student("Shahrukh")

print(student1.name)
print(student2.name)

print(student1.university)
print(student2.university)
print(Student.university)



# Instance attribute	Class attribute
# Object-specific data	Class-level data
# Example: self.name	Example: university
# Har object ki value alag ho sakti hai	Instances normally shared class value access karte hain
# Dhyan rahe: Agar instance par same naam ka attribute assign karte ho, toh woh class attribute ko override nahi karta; woh instance attribute create karta hai jo normal attribute lookup mein class attribute ko shadow karta hai.



# Instance methods and class methods
# Instance method
# self receive karta hai aur object ke data ke saath kaam karta hai.

class Calculator:
    def add(self, a, b):
        return a + b


calc = Calculator()
print(calc.add(10, 20))


# Class method
# @classmethod use karta hai aur pehle parameter ke roop mein cls receive karta hai.
class Student:
    university = "JECRC University"

    @classmethod
    def change_university(cls, name):
        cls.university = name


Student.change_university("Example University")
print(Student.university)


# Yeh example class attribute change karta hai, isliye shared class value update ho jaati hai.


# Static method
# @staticmethod aise utility behaviour ke liye useful hai jise self ya cls ki zaroorat nahi hoti.
class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.multiply(5, 4))





print("\n")
# Practical example — Student Management
class Student:
    university = "JECRC University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("University:", self.university)

    def is_passed(self):
        return self.marks >= 40


student1 = Student("Aman", 85)
student2 = Student("Rahul", 32)

student1.display_info()
print("Passed:", student1.is_passed())

print()

student2.display_info()
print("Passed:", student2.is_passed())










