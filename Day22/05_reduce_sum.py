from functools import reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)