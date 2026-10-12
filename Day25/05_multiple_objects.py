class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"{self.brand}: ₹{self.price}")


mobile1 = Mobile("Samsung", 20000)
mobile2 = Mobile("Apple", 60000)

mobile1.display()
mobile2.display()