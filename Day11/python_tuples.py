


# What is a Tuple?
# A tuple is an ordered, unchangeable collection of values.

fruits = ("apple", "banana", "mango")

# Tuples usually use round brackets ()



numbers = (10, 20, 30, 40)

languages = ("Python", "Java", "C++")

data = ("Shahrukh", 21, 78.5, True)

# Python allows different data types inside a tuple.




numbers = (10, 20, 30, 40)
print(numbers[0])
print(numbers[2])

print(numbers[-1]) #negative indexing also works in tuples



# Tuple Indexing

"""
Tuple:

(10, 20, 30, 40)

↓   ↓   ↓   ↓
0   1   2   3

-4  -3  -2  -1
"""


# Tuple Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

"""
Same slicing rule:-

[1:4]

[start : stop]

stop is not included

"""


# Why Use Tuples?
# Suppose you have fixed information:-
coordinates = (26.9124, 75.7873)

# You don't want those values accidentally changed.

# A tuple communicates:-
# This collection should remain fixed.



# Other examples:-
rgb = (255, 255, 255)
date = (28, 9, 2026)
dimensions = (1920, 1080)






# 20% Knowledge → 80% Impact:-


student = ("Shahrukh", 21, "BCA")

# Access
student[0]

# Negative index
student[-1]

# Slicing
student[0:2]

# Check
"BCA" in student

# Count
student.count("BCA")

# Index
student.index("BCA")

# Unpacking
name, age, course = student

# Immutability
student[0] = "Aman"
# ❌ Not allowed


