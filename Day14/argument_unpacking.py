# Unpacking Arguments 🔥
# Remember Day 11 tuple unpacking?
# You can also unpack arguments.

def add(a, b, c):
    return a + b + c

numbers = (10, 20, 30)

print(add(*numbers))

# *numbers means:-
# (10, 20, 30)
#      ↓
# 10, 20, 30


# Similarly dictionaries can be unpacked using **
def student(name, age):
    print(name, age)

data = {
    "name": "Avi",
    "age": 14
}

student(**data)










