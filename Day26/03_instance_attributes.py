class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


mobile1 = Mobile("Samsung", 20000)
mobile2 = Mobile("Apple", 60000)

print(mobile1.brand, mobile1.price)
print(mobile2.brand, mobile2.price)