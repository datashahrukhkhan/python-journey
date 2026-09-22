# Python Learning Journey
# Day 5 - Conditions


# 1. IF CONDITION
age = 20
if age >= 18:
    print("You are eligible to vote.")


# 2. IF - ELSE
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# 3. IF - ELIF - ELSE
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")


# 4. COMPARISON
number = 10
if number > 0:
    print("Number is positive.")
elif number < 0:
    print("Number is negative.")
else:
    print("Number is zero.")


# 5. LOGICAL OPERATORS
age = 21
has_id = True
if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")


# 6. NESTED IF
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("You can enter.")
    else:
        print("ID required.")

else:
    print("You must be 18 or older.")
