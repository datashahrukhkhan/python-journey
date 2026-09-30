# Nested Dictionaries 🔥
# A dictionary can contain another dictionary.

students = {
    "student1": {
        "name": "Avi",
        "age": 18
    },
    "student2": {
        "name": "Suman",
        "age": 16
    }
}


# Access:-
print(students["student1"]["name"])

for student in students.values():
    print(student["name"], "-", student["age"])












