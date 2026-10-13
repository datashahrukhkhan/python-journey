class Calculator:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(Calculator.is_even(10))
print(Calculator.is_even(7))