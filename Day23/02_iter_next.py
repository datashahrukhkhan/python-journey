names = ["Aman", "Rahul", "Shahrukh"]

iterator = iter(names)

while True:
    name = next(iterator, None)

    if name is None:
        break

    print(name)



# This code demonstrates the use of an iterator and the next() function to iterate through a list of names.

# syntax:
# iterator = iter(iterable)
# that means we create an iterator object from the iterable (in this case, the list of names) using the iter() function.

# next(iterator, default) 
# that means if the iterator is exhausted, it will return the default value instead of raising StopIteration exception.

# logic:
# 1. We create an iterator object from the list of names using the iter() function.
# 2. We use a while loop to continuously call the next() function on the iterator
# 3. The next() function retrieves the next item from the iterator. If there are no more items, it returns None.
