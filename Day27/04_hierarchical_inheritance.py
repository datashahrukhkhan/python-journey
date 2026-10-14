class Animal:
    def eat(self):
        print("Eating food")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()