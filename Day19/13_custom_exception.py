class AgeError(Exception):
    pass


age = int(input("Enter your age: "))

try:
    if age < 18:
        raise AgeError("Age must be 18 or above.")

    print("You are eligible.")

except AgeError as e:
    print("Error:", e) 