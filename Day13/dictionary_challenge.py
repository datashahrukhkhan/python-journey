# Challenge
# Create a simple student database:-

students = {
    "student1": {
        "name": "Arshd",
        "marks": 85
    },
    "student2": {
        "name": "Mo_Naaj",
        "marks": 78
    },
    "student3": {
        "name": "Sahid_Arman",
        "marks": 92
    }
}

print(students["student1"]["name"])

for student in students.values():
    print(student["name"], "-", student["marks"])









