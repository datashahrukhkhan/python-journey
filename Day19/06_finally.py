try:
    number = int(input("Enter number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")