class LivingBeing:
    def live(self):
        print("Living being is alive")


class Animal(LivingBeing):
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()
dog.live()
dog.eat()
dog.bark()