lines = [
    "Python\n",
    "JavaScript\n",
    "React\n",
    "Azure\n"
]

with open("skills.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("Skills saved successfully.")