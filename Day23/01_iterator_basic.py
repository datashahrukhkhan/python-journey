fruits = ["Apple", "Mango", "Banana"]

fruit_iterator = iter(fruits)

print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))


# here, we are using the iter() function to create an iterator object from the list of fruits. 
# The next() function is then used to retrieve the next item from the iterator. 
# Each call to next() returns the next fruit in the list until all items have been retrieved.