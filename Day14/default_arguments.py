# Default Arguments 🔥
# A function can have a default value.

def greet(name="Soyal"):
    print("Hello", name)

greet()

# But:-
greet("Shehzad")

# Output:- Hello Shehzad
# The provided argument overrides the default.


# Multiple Default Arguments
def student(name="Arman", course="BA"):
    print(name)
    print(course)

student()
student(course="MA")


# Important Rule for Default Arguments ⚠️
# This is wrong:-
# def student(name="Shahrukh", age):
#     print(name, age)
# Python doesn't allow a non-default parameter after a default parameter.

# Correct:-
def student(name, age=21):
    print(name, age)




