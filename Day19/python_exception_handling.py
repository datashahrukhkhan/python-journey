# Python Exception Handling
# Agar program run karte time error aa jaye, to program ko crash hone se kaise bachayein?

# Iske liye Python mein Exception Handling use hoti h


# Exception kya hoti hai?
# Program run karte waqt agar koi unexpected problem aaye, Python exception raise kar sakta hai.
# Example:-
number = int(input("Enter number: "))
print(number)

# Agar user input kare:-
# abc

# to error:-
# ValueError

# Program crash ho jayega.
# Exception handling se hum is situation ko handle kar sakte h



# Error vs Exception
# Simple way:-
# Error
# Program mein serious problem ya invalid situation.

# Exception
# Runtime ke time aane wali problem jise hum programmatically handle kar sakte hain.

# Example:- 10/0
# Python:- ZeroDivisionError




# Basic try-except
# Syntax:-
# try:
#     # risky code
# except:
#     # error handle


# Example:-
try:
    number = int(input("Enter number: "))
    print(number)
except:
    print("Invalid input")


# Agar user:-
# 25

# output: 25

# Agar user:-
# abc

# output: Invalid input
# Program crash nahi karega.




# Flow samjho:-
#         try
#          ↓
#    Code execute karo
#          ↓
#     ┌────┴────┐
#     ↓         ↓
#  No Error   Error
#     ↓         ↓
#  Continue   except
#               ↓
#         Handle Error



# Specific Exception Handle karna ⭐
# Blank except use karne ke bajay specific exception handle karna better practice hai.

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid number.")



# ZeroDivisionError
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")



# Multiple except
# Different errors ko separately handle kar sakte he.

try:
    number = int(input("Enter number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")



# else
# else tab execute hota hai jab koi exception nahi aati.
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)

# Flow:-
# try
#  ↓
# Error?
#  ├── Yes → except
#  │
#  └── No → else



# finally
# finally almost always execute hota hai, chahe exception aaye ya na aaye.

try:
    number = int(input("Enter number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")



# 🧠 Memory Trick
# try     → Try this code
# except  → Handle error
# else    → No error hua
# finally → Ye last mein karna hi hai



# Complete Structure
# try:
#     # risky code

# except SomeError:
#     # error handling

# else:
#     # successful execution

# finally:
#     # cleanup




# Exception as e
# Error ka actual message dekhna ho:
try:
    result = 10 / 0

except Exception as e:
    print("Error:", e)

# Output:-
# Error: division by zero

# Yahan:-
# as e
# exception object ko e variable mein store karta hai.





# Multiple Exceptions Together
# Agar same handling chahiye:-
try:
    number = int(input("Enter number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input.")


# Common Python Exceptions
# Exception	                    Example
# ValueError	                Invalid value conversion
# TypeError	                    Wrong data type operation
# ZeroDivisionError	            Number / 0
# IndexError	                Invalid list index
# KeyError	                    Missing dictionary key
# FileNotFoundError	            File doesn't exist
# NameError	                    Variable doesn't exist
# AttributeError	            Invalid attribute/method



# ValueError
try:
    age = int("hello")

except ValueError:
    print("Cannot convert to integer.")



# TypeError
try:
    result = "10" + 5

except TypeError:
    print("Cannot add string and integer.")



# IndexError
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist.")


# KeyError
student = {
    "name": "Shahrukh",
    "age": 22
}

try:
    print(student["marks"])

except KeyError:
    print("Marks key not found.")



# FileNotFoundError
try:
    with open("unknown.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File does not exist.")


# raise
# Kabhi-kabhi hume khud exception generate karni hoti hai.
# Use:- raise

# example:- 
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")


# raise with Function
def withdraw(amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    return amount


print(withdraw(500))



# Custom Exception
# Python mein apni exception class bhi bana sakte ho.

class AgeError(Exception):
    pass

# use:-
age = 15

try:
    if age < 18:
        raise AgeError("Age must be 18 or above")

except AgeError as e:
    print("Error:", e)








