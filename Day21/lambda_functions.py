# Lambda Functions
# Aaj hum Python ka Lambda Function seekhenge. Ye small/short functions ke liye useful hai, 
# especially map(), filter() aur sorted() ke saath.


# Concept / Definition
# Normal function:-
from ast import Lambda
from symtable import Function


def square(x):
    return x * x

print("Normal function:", square(5))


# Lambda version:-
square = lambda x: x * x
print("Lambda function:", square(5))


# Formula yaad rakho
# lambda arguments: expression

# Lambda = one-line anonymous function


# Why Lambda?
# Jab function:-
# - bahut small ho
# - sirf ek expression return karta ho
# - ek hi jagah temporarily use karna ho
# tab lambda useful hota h


# another Example:-
add = lambda a, b: a + b

print(add(10, 20))



# Lambda with One Argument
double = lambda x: x * 2

print(double(5))


# Lambda with Multiple Arguments
multiply = lambda a, b: a * b

print(multiply(5, 4))


# Lambda with Condition
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))



# Lambda with sorted()
# Ye interview + practical use ke liye important h

students = [
    ("Aman", 80),
    ("Rahul", 95),
    ("Shahrukh", 55)
]

# Ascending order:-
students.sort(key=lambda student: student[1])
print(students)

# Descending order:-
students.sort(key=lambda student: student[1], reverse=True)
print(students)

# in strings
# strings ko sort karne ke liye bhi lambda use hota h
names = ["shahrukh", "avi", "aman", "aayat"]

names.sort(key=lambda name: len(name))
print(names)



# Normal Function	                       Lambda

# def use karta hai	                       lambda use karta hai
# Multiple statements possible	           Generally single expression
# Complex logic ke liye better	           Small logic ke liye better
# Function ka naam usually hota hai	       Anonymous function ho sakta hai



numbers = [10, 5, 8, 20, 3, 15]

square_numbers = list(map(lambda x: x * x, numbers))

print("Original:", numbers)
print("Squares:", square_numbers)


# 🧠 Important Keywords
# - lambda
# - anonymous function
# - arguments
# - expression
# - return
# - sorted()
# - key=
# - reverse=True




# 1. What is a lambda function?
# Answer:-
# A lambda function is an anonymous function in Python that can have any number of arguments but can only have one expression. It is defined using the lambda keyword and is often used for short, simple functions that are used once or in combination with other functions like map(), filter(), and sorted().
# A lambda function is a small anonymous function that can take multiple arguments but contains a single expression.


# 2. What is the syntax of lambda?
# Answer:-
# lambda arguments: expression

# 3. Can lambda have multiple arguments?
# Answer:-
# Yes, a lambda function can accept multiple arguments.
# Example: lambda a, b: a + b



# 4. Can we use multiple statements inside lambda?
# Answer:
# No. Lambda is designed for a single expression.


# When should we use lambda?
# Answer:-
# We should use lambda for short and simple operations where creating a full function is unnecessary.


# 💡 Memory Trick
# LAMBDA = Less code + Anonymous + Mini function + Basic expression + Direct use + Action







