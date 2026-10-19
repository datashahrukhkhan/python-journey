
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")

SUBJECTS = [
    "English",
    "Hindi",
    "Science",
    "Social Science",
    "Maths",
    "Computer Science"
]


def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid student data format.")
            return []

        return data

    except json.JSONDecodeError:
        print("students.json is invalid. Please check the file.")
        return []

    except OSError as error:
        print("Could not load data:", error)
        return []


def save_students(students):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True

    except OSError as error:
        print("Could not save data:", error)
        return False


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def get_marks():
    marks = {}

    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject} marks (0-100): "))

                if 0 <= score <= 100:
                    marks[subject] = score
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a number.")

    return marks


def show_result(student):
    marks = student["marks"]

    print("\n========== STUDENT RESULT ==========")
    print("ID:", student["id"])
    print("Name:", student["name"])

    for subject in SUBJECTS:
        print(f"{subject}: {marks[subject]:g}")

    total = sum(marks[subject] for subject in SUBJECTS)
    percentage = total / 6
    average = total / 6

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n========== STUDENT RESULT ==========")
    print(f"Total: {total:g}/600")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Average: {average:.2f}")
    print("Grade:", grade)
    print("====================================")


def add_student(students):
    student_id = input("Student ID: ").strip()

    if not student_id:
        print("ID cannot be empty.")
        return

    if find_student(students, student_id):
        print("This ID already exists.")
        return

    name = input("Student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student = {
        "id": student_id,
        "name": name,
        "marks": get_marks()
    }

    students.append(student)

    if save_students(students):
        print("Student added successfully!")
        show_result(student)
    else:
        students.pop()


def view_students(students):
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No students found. Use ADD first.")
        return

    for student in students:
        marks = student.get("marks", {})

        if not isinstance(marks, dict):
            print(f"ID: {student.get('id', 'N/A')} - Old data format")
            continue

        if not all(subject in marks for subject in SUBJECTS):
            print(f"ID: {student.get('id', 'N/A')} - Incomplete marks")
            continue

        total = sum(marks[subject] for subject in SUBJECTS)
        percentage = total / 6

        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Total: {total:g}/600 | "
            f"Percentage: {percentage:.2f}%"
        )


def search_student(students):
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)

    if student:
        show_result(student)
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Choose a subject:")

    for index, subject in enumerate(SUBJECTS, start=1):
        print(f"{index}. {subject}")

    try:
        choice = int(input("Subject number (1-6): "))

        if choice < 1 or choice > 6:
            print("Invalid subject number.")
            return

    except ValueError:
        print("Enter a valid number.")
        return

    subject = SUBJECTS[choice - 1]

    try:
        score = float(input(f"New {subject} marks (0-100): "))

        if not 0 <= score <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Enter a valid number.")
        return

    old_score = student["marks"].get(subject)
    student["marks"][subject] = score

    if save_students(students):
        print("Marks updated!")
        show_result(student)
    else:
        student["marks"][subject] = old_score


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirm = input("Type YES to confirm deletion: ").strip()

    if confirm != "YES":
        print("Deletion cancelled.")
        return

    index = students.index(student)
    students.pop(index)

    if save_students(students):
        print("Student deleted.")
    else:
        students.insert(index, student)


def class_average(students):
    valid_students = [
        student for student in students
        if isinstance(student.get("marks"), dict)
        and all(subject in student["marks"] for subject in SUBJECTS)
    ]

    if not valid_students:
        print("No complete student results available.")
        return

    percentages = [
        sum(student["marks"][subject] for subject in SUBJECTS) / 6
        for student in valid_students
    ]

    print("Students:", len(valid_students))
    print(f"Class average: {sum(percentages) / len(percentages):.2f}%")


def main():
    students = load_students()

    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("Type a command and press Enter.")

    while True:
        print("\nCommands: ADD | VIEW | SEARCH | UPDATE")
        print("          AVERAGE | DELETE | EXIT \n")

        command = input("Enter Command: ").strip().upper()

        if command == "ADD":
            add_student(students)
        elif command == "VIEW":
            view_students(students)
        elif command == "SEARCH":
            search_student(students)
        elif command == "UPDATE":
            update_student(students)
        elif command == "AVERAGE":
            class_average(students)
        elif command == "DELETE":
            delete_student(students)
        elif command == "EXIT":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Type VIEW, ADD, or EXIT.")


if __name__ == "__main__":
    main()
