with open("data.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print("First:", first_line.strip())
print("Second:", second_line.strip())