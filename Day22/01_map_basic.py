numbers = [1, 2, 3, 4, 5]

def double(x):
    return x * 2

result = list(map(double, numbers))

print("Original:", numbers)
print("Doubled:", result)