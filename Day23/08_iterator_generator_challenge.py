def generate_even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


def main():
    print("Even numbers from 2 to 20:")

    for number in generate_even_numbers(20):
        print(number)


if __name__ == "__main__":
    main()


# This code demonstrates the use of a generator function to generate even numbers up to a specified limit.
# syntax:
# def generator_function():
# that means we define a function that contains one or more yield statements.

# yield value
# that means we use the yield statement to produce a value and pause the function's execution.


