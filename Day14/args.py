
# *args — Multiple Positional Arguments 🔥
# What if you don't know how many arguments the function will receive?

# Use:-  *args

# Example:-
def add(*numbers):
    print(numbers)

add(10, 20, 30)
# Notice:- 
# *args becomes a tuple.

# You can loop through it:-
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20, 30))
print(add(1, 2,))
print(add(1, 2, 4))
print(add(1, 2, 3, 4))
print(add(10, 20, 30, 40, 50))

# Why *args?
# Without *args:-
def add(a, b):
    return a + b

# Only two values.
# With:-
# def add(*numbers):

# You can pass:
# 2 values
# 3 values
# 10 values
# 100 values
# This makes functions flexible.
