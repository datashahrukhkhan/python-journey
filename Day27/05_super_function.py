class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student = Student("Shahrukh", "BCA")
student.display()