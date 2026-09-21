# Day 4 - Operators
# Python Learning Journey


# 1. Arithmetic Operators

a = 10
b = 3

print("Arithmetic Operators")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 2. Comparison Operators

print("\nComparison Operators")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# 3. Logical Operators

age = 21
has_id = True

print("\nLogical Operators")

print("Age >= 18 AND has ID:", age >= 18 and has_id)
print("Age < 18 OR has ID:", age < 18 or has_id)
print("NOT has ID:", not has_id)



# 4. Assignment Operators


print("\nAssignment Operators")

number = 10

number += 5
print("After += 5:", number)

number -= 3
print("After -= 3:", number)

number *= 2
print("After *= 2:", number)

number /= 4
print("After /= 4:", number)



# Membership Operators
# in & not in
skills = ["Python", "AWS", "SQL"]

print("\nMembership Operators")

print("Python" in skills)
print("Java" in skills)
print("Java" not in skills)