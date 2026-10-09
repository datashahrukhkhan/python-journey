# Program user se student information lega aur file mein save karega.

name = input("Enter student name: ")
course = input("Enter course: ")
age = input("Enter age: ")

with open("students.txt", "a", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Age: {age}\n")
    file.write("-" * 30 + "\n")

print("Student information saved successfully.")

# Next student add karoge to existing data delete nahi hoga because:-
# "a"
# use kiya h










