from functools import reduce

numbers = [2, 5, 8, 11, 14, 17, 20]
print("Original numbers:", numbers)

# 1. Square every number
squares = list(map(lambda x: x * x, numbers))

# 2. Select even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 3. Select numbers greater than 10
greater_than_10 = list(filter(lambda x: x > 10, numbers))

# 4. Calculate sum of all numbers
total = reduce(lambda a, b: a + b, numbers)

print("Squares:", squares)
print("Even numbers:", evens)
print("Greater than 10:", greater_than_10)
print("Total:", total)