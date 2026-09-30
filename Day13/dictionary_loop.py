# Loop Through a Dictionary

student = {
    "name": "Mr.Shahrukh-khan",
    "age": 22,
    "course": "BCA-5th_sem"
}

# Only keys
for key in student:
    print(key)

print("\n")

# Only values
for value in student.values():
    print(value)

print("\n")

# Keys + Values 🔥
for key, value in student.items():
    print(key, ":", value)


print("\n")


# Check if a Key Exists
# Use in 
student = {
    "name": "Aaryan",
    "age": 32
}

print("name" in student) #checks keys, not values
print("salary" in student)


