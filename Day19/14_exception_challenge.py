# Ek calculator banao jo:
# - User se 2 numbers le
# - Division kare
# - Invalid input handle kare
# - Zero division handle kare
# - Finally message print kare


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Calculator execution completed.")











