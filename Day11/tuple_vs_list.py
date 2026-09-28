# List = changeable collection
# Tuple = unchangeable collection


# Lists are mutable, meaning you can change their content after they are created. For example, you can add, remove, or modify elements in a list.
fruits = ["apple", "banana", "mango"]

fruits[0] = "orange" # This is allowed because lists are mutable


# Tuples are immutable, meaning once the
# y are created, their content cannot be changed. You cannot add, remove, or modify elements in a tuple.
fruits = ("apple", "banana", "mango")

fruits[0] = "orange" # This will raise an error because tuples are immutable



# Why is this happening?

# Because tuples are immutable.

# List
#  ↓
# Mutable
#  ↓
# Can change

# Tuple
#  ↓
# Immutable
#  ↓
# Cannot change





# List vs Tuple
'''
Feature	    List	Tuple
Syntax	    []	    ()
Ordered	    ✅	   ✅
Mutable	    ✅	   ❌
Indexing	✅	   ✅
Slicing	    ✅	   ✅
count()	    ✅	   ✅
index()	    ✅	   ✅
append()	✅	   ❌
remove()	✅	   ❌
'''



# Easy memory trick:-
# LIST  → CHANGE
# TUPLE → FIX