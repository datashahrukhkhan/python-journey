numbers = [100, 200]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iteration completed")


# This code demonstrates the use of an iterator and the next() function to iterate through a list of numbers.
# syntax:-
# iterator = iter(iterable)
# that means we create an iterator object from the iterable (in this case, the list of
# (numbers) using the iter() function.

# next(iterator)
# that means we retrieve the next item from the iterator. If there are no more items,
# it raises a StopIteration exception.





