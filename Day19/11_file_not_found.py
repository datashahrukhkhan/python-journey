try:
    with open("unknown.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")