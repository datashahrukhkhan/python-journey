class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


employee = Employee()
developer = Developer()

employee.work()
developer.work()