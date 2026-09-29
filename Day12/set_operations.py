
# Set Operations 🔥🔥🔥

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union -> Everything from both sets
print("A | B ",A | B)


# Intersection
# Find values common to both sets.
C = {1, 2, 3, 4}
D = {3, 4, 5, 6}
print("C & D ",C & D)

# Difference
# Values that exist in A but not B
E = {1, 2, 3, 4}
F = {3, 4, 5, 6}
print("E - F ",E - F)


# Symmetric Difference
# Values that are in either set, but not in both.
G = {1, 2, 3, 4}
H = {3, 4, 5, 6}

print("G ^ H ",G ^ H)


# Visual Understanding:-
"""
        A               B
    ┌─────────┐     ┌─────────┐
    │ 1   2   │     │   5  6  │
    │    3 ┌──┼─────┼──┐ 4    │
    │      │  │     │  │      │
    └──────┼──┘     └──┼──────┘
           └────────────┘
             Common

So:-

Union                → Everything
Intersection         → Common
Difference           → Only in first
Symmetric Difference → Not common

"""

print("\n")

# Remove Duplicates from a List 🔥
numbers = [10, 20, 20, 30, 30, 40]
print("numbers: ",numbers)

unique_numbers = list(set(numbers))

print("unique_numbers: ",unique_numbers)
# ⚠️ One important detail: converting through a set does not guarantee the original order. If preserving order matters, use a different approach.

print("\n")

# Loop Through a Set
languages = {"Python", "Java", "C++"}
print("language:- ",languages)

for language in languages:
    print(language)






print("\n")


# Sets Automatically Remove Duplicates 🔥 This is one of the most important features.

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

# Output will contain only unique values:- {10, 20, 30}



# -------------------------------------------------------------------------------------------------------------------
print("\n")



# Creating a Set:-
fruits = {"apple", "banana", "mango"}

print(fruits)



# -------------------------------------------------------------------------------------------------------------------
print("\n")




# You can also create an empty set, but be careful
my_set = set()
print(type(my_set))

my_set = {}
# creates an empty dictionary, not an empty set
print(type({}))




# -------------------------------------------------------------------------------------------------------------------
print("\n")



# Adding Elements:
# Use add()
fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)

# If i add an existing value:-

fruits.add("apple")

# nothing changes. Why?
# Because sets contain only unique values.


# -------------------------------------------------------------------------------------------------------------------
print("\n")


# Add Multiple Values:-
# update()
fruits = {"apple", "banana"}

fruits.update(["mango", "orange", "grapes"])

print(fruits)


# Now all those elements are added
# You can also update using another set:-
a = {1, 2, 3}
b = {4, 5, 6}

a.update(b)

print(a)




# -------------------------------------------------------------------------------------------------------------------
print("\n")


# Remove Elements
# remove()
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")
print(fruits)

# But if the element doesn't exist:- ❌ Python raises an error
# fruits.remove("orange")
# print(fruits)

# discard()
fruits.discard("orange")
print(fruits)
# If "orange" doesn't exist, Python doesn't raise an error

print("\n")

# pop()
fruits = {"apple", "banana", "mango"}



fruits.pop()
print(fruits)
# pop() removes and returns an arbitrary element from the set
