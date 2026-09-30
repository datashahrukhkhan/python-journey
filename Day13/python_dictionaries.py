# A dictionary stores data as:-
# key → value
# Dictionaries are mutable

# student
#    ↓
# ┌──────────┬───────────┐
# │ Key      │ Value     │
# ├──────────┼───────────┤
# │ name     │ Shahrukh  │
# │ age      │ 21        │
# │ course   │ BCA       │
# └──────────┴───────────┘

# dictionary = {
#     "key": value,
#     "key": value
# }


student = {
    "name": "Shahrukh",
    "age": 21,
    "course": "BCA",
    "marks": 85
}

# student = ["Shahrukh", 21, "BCA", 85]

print(student)

# The syntax is:- dictionary["key"]
print(student["name"])
print(student["marks"])
print(student["age"])

# Clearly means marks. That's the power of key-value data.


print("\n")

# get() — Safer Access
student.get("name")
print(student.get("name"))


# print(student["salary"])
# If "salary" doesn't exist:- KeyError

# But:-
print(student.get("salary"))
# returns:-None

# You can also provide a default:-
print(student.get("salary", 0))


print("\n")


# Add a New Key
student = {
    "name": "Aayat",
    "age": 20
}

student["course"] = "BBA"

print(student)


print("\n")

# Update a Value
# If the key already exists:-
student["age"] = 19

# It updates the existing value
student["name"] = "Sapna"
print(student)



print("\n")
student = {
    'name': 'Sapna', 
    'age': 19, 
    'course': 'BBA'
}
# Remove Data
# pop()
# student.pop("age")
print(student.pop("age")) #Removes the key and returns its value
print(student) #not show key and value both


# del
del student["course"]
print(student)
# Deletes the key-value pair


# clear()
student.clear()
print(student.clear())  #show output none
print(student) #Removes everything



# Dictionary vs Other Data Structures

# Structure	          Main-Idea
# List	        <-    Ordered collection
# Tuple	        <-    Ordered + fixed
# Set	        <-    Unique values
# Dictionary	<-    Key → Value


# Memory trick:-
# List       → Position
# Tuple      → Fixed data
# Set        → Unique data
# Dictionary → Meaningful keys



# --------------------------------------------------------------------------------------------------------
student = {
    'name': 'Sapna', 
    'age': 19, 
    'course': 'BBA'
}

# ⚠️ Common Mistakes
# Mistake 1 — Using an index
# This is wrong:-

# student[0]  
# Dictionaries use keys, not numerical positions.

# Use:-
student["name"]

print("\n")
# Mistake 2 — Confusing keys() and values()
# "name" in student 
print("name" in student) # checks the key.

# To check a value:-
# "Shahrukh" in student.values()
print("Shahrukh" in student.values()) # checks the value



# Mistake 3 — Missing comma
# Wrong:-
# student = {
#     "name": "Shahrukh"
#     "age": 21
# }

# Correct:-
student = {
    "name": "Shahrukh",
    "age": 21
}





