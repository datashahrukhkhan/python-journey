# Python Decorators

# aaj hum Python ka ek important intermediate concept seekhenge: Decorators. Interviews mein bhi is topic par questions pooche jaate hain, aur real projects mein decorators ka use logging, authentication aur timing jaise tasks ke liye hota h.

# Concept / Definition
# Decorator ek function hota hai jo kisi doosre function ke behaviour ko modify ya extend karta hai, bina us function ka original code change kiye.


# Without decorator
def greet():
    print("Hello, Shahrukh!")

def welcome():
    print("Function started")
    greet()
    print("Function finished")

welcome()

# Yahan welcome() ko manually extra work karna pad raha h

print("\n\n")
# decorator
# Decorator banane ke liye ek function doosre function ko argument ke roop mein leta hai aur generally ek wrapper function return karat h

def my_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper


@my_decorator
def greet():
    print("Hello, Shahrukh!")


greet()


# Code ko samjho
# - my_decorator(func) — original function receive karta hai.
# - wrapper() — extra behaviour add karta hai.
# - func() — original function execute karta hai.
# - return wrapper — enhanced function return karta hai.
# - @my_decorator — decorator apply karne ka shortcut hai.
# Important: @my_decorator roughly greet = my_decorator(greet) ke equivalent h


# Decorator with arguments
# Pichhle example mein wrapper sirf aise functions ke liye tha jo arguments nahi lete. General-purpose decorator ke liye *args aur **kwargs use kar sakte hain.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calculating...")
        result = func(*args, **kwargs)
        print("Calculation completed")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


answer = add(10, 20)
print("Result:", answer)





# Practical example — Function execution time
# Kabhi-kabhi humein measure karna hota hai ki koi function kitna time leta h
import time
from functools import wraps


def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper


@calculate_time
def calculate_sum():
    return sum(range(1_000_001))


print("Total:", calculate_sum())

