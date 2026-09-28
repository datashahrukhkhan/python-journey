# Tuple Unpacking
# This is one of the most useful tuple concepts.

student = ("Shahrukh", 21, "BCA")

name, age, course = student

print(name)
print(age)
print(course)

"""
("Shahrukh", 21, "BCA")
    ↓       ↓      ↓
    name    age   course
"""

# This becomes very useful when working with functions and data.

# --------------------------------------------------------------------------------------------------------------------------


# Returning Multiple Values from a Function
# Python can return multiple values

def student_info():
    return "Shahrukh", 21, "BCA"

name, age, course = student_info()

print(name)
print(age)
print(course)

# Python internally treats the returned values as a tuple
# This is one reason tuples matter