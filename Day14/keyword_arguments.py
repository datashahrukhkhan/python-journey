# Keyword Arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Shahrukh", 21)

print("\n")

# you can explicitly specify:-
student(name="Shahrukh", age=21)

print("\n")

# Now order doesn't matter:-
student(age=21, name="Shahrukh")


# Output same rahega.

# Why useful?
# Code zyada readable hota hai:

# age=21
# name="Shahrukh"

# clearly tells Python what each value means.




