class Employee:
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Aman")
employee2 = Employee("Shahrukh")

print(employee1.name, employee1.company)
print(employee2.name, employee2.company)