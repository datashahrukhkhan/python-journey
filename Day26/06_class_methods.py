class Student:
    school = "ABC School"

    @classmethod
    def set_school(cls, school_name):
        cls.school = school_name


Student.set_school("XYZ School")
print(Student.school)