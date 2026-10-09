import os

if os.path.exists("skills.txt"):
    os.remove("skills.txt")
    print("File deleted.")
else:
    print("File not found.")