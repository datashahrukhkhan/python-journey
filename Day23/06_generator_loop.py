def multiplication_table(number):
    for i in range(1, 11):
        yield number * i


for result in multiplication_table(5):
    print(result)


# This code demonstrates the use of a generator function to create a multiplication table for a given number.
# syntax:
# def generator_function():
# that means we define a function that contains one or more yield statements.

# yield value
# that means we use the yield statement to produce a value and pause the function's execution.














