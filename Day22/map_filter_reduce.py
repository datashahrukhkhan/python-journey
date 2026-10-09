# map(), filter() and reduce()
# aaj hum Python ke 3 useful tools seekhenge. Ye lists aur data ke saath kaam karne mein help karte h


# Concept / Definition :-
# Function     Simple meaning
# map()	    -> Har item par operation perform karna
# filter()  -> Condition ke basis par items select karna
# reduce()  -> Saare items ko combine karke ek result banana


# Yaad rakho:- Map = Transform, Filter = Select, Reduce = Combine.

# map() — Har item ko transform karo
# Example: Har number ka square nikalna.

numbers = [1, 2, 3, 4, 5]
print("numbers:", numbers)

def square(x):
    return x * x

result = list(map(square, numbers))

print("result:", result)

print("\n")
# Lambda ke saath:-
numbers = [6, 7, 8, 9, 10]
print("numbers:", numbers)

result = list(map(lambda x: x * x, numbers))

print("result:", result)

# map() ek iterable return karta hai, isliye result ko list ke form mein dekhne ke liye list() use kiya.



print("---------------------------------------------------------------")


# filter() — Condition ke basis par select karo

# Example:- Sirf even numbers select karna.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("numbers:", numbers)

result = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", result)


print("\n")
# Another example:-
marks = [25, 45, 80, 32, 90, 60]
print("marks:", marks)

passed = list(filter(lambda mark: mark >= 40, marks))

print("Passed students:", passed)


print("---------------------------------------------------------------")

# reduce() — Items ko combine karo
# reduce() ko use karne ke liye functools module se import karna hota hai.

# Example: List ke saare numbers ka sum.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
print("numbers:", numbers)

result = reduce(lambda a, b: a + b, numbers)

print("Sum of numbers:", result)


print("\n")
# Another example — product of all numbers:-
from functools import reduce

numbers = [2, 3, 4]
print("numbers:", numbers)

result = reduce(lambda a, b: a * b, numbers)

print("Product of numbers:", result)




# Complete comparison:-

# Feature	        map()	                    filter()	        reduce()
# Purpose	        Transform	                Select	            Combine
# Result	        One result per input item	Selected items	    Usually one accumulated result
# Example	        Square numbers	            Even numbers	    Sum of numbers
# Import required	No	                        No	                functools se





