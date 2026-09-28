

# Single-Element Tuple ⚠️

numbers = (10)  #is not a tuple. It's simply an integer.
numbers = (10,)  # This is a tuple with one element.
# The comma is important 👆
# One-element tuple needs a comma

print(type((10)))
print(type((10,)))



# ⚠️ Common Mistake

# Don't think: "Tuple is just a list with ()."
# That's incomplete.
# The important difference is mutability.


my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# You can change:-
my_list[0] = 100

# But not:-
my_tuple[0] = 100






















