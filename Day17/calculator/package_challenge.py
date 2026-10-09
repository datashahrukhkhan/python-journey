from package_demo.addition import add
from package_demo.subtraction import subtract


def main():
    num1 = 20
    num2 = 10

    print("Number 1:", num1)
    print("Number 2:", num2)

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))


if __name__ == "__main__":
    main()