from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)