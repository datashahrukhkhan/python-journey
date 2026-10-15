class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def set_temperature(self, celsius):
        if celsius < -273.15:
            print("Invalid temperature")
            return

        self.__celsius = celsius

    def get_temperature(self):
        return self.__celsius


temperature = Temperature(25)

print(temperature.get_temperature())

temperature.set_temperature(30)
print(temperature.get_temperature())

temperature.set_temperature(-300)