def simple_generator():
    yield "First"
    yield "Second"
    yield "Third"


generator = simple_generator()

print(next(generator))
print(next(generator))
print(next(generator))





# This code demonstrates the use of a generator function in Python.
# syntax:
# def generator_function():
# that means we define a function that contains one or more yield statements.

# yield value
# that means we use the yield statement to produce a value and pause the function's execution.

