class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is moving")


car = Car()
car.start()
car.drive()