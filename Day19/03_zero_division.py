try:
    number = int(input("Enter number: "))

    result = 100 / number

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")