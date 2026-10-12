class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40


student1 = Student("Aman", 85)
student2 = Student("Rahul", 32)

student1.display()
print("Passed:", student1.is_passed())

student2.display()
print("Passed:", student2.is_passed())