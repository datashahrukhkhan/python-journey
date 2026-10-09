# Day 16 = Modules
# Day 17 = Packages
# Day 18 = Files ke andar data read/write karna


# File Handling kya hota hai?

# Python se hum files ko:
# - Create kar sakte hain
# - Read kar sakte hain
# - Write kar sakte hain
# - Append kar sakte hain
# - Delete kar sakte hain


# from setuptools import Command


# Command files:
# .txt
# .csv
# .json



# open() Function
# File handling ka basic function:- open()

# syntex:-
# open("filename", "mode")

# example:-
# file = open("data.txt", "r")

# yha pr:-
# data.txt → file name
# r        → read mode



# File Modes
# Mode	            Meaning
# r	                Read
# w	                Write
# a	                Append
# x	                Create
# r+	            Read + Write
# w+	            Write + Read
# a+	            Append + Read


# 🧠 Memory Trick
# r → Read
# w → Write
# a → Add
# x → Create



# ----------------------------------------------------------------------------------------------------
# Read File
# Suppose:-
# Day18/
# └── data.txt


# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()


file = open("Day18/data.txt", "r", encoding="utf-8")
print(file.read())
file.close()



# close() kyu?
# File open karne ke baad:
# file.close()
# karna good practice h.

# Flow:-
# open()
#   ↓
# Use file
#   ↓
# close()
# Agar close nahi karoge to resources unnecessarily open reh sakte hain.


# with open() — BEST PRACTICE ⭐
# Professional Python mein ye approach prefer karo:

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)


from pathlib import Path

file_path = Path(__file__).parent / "data.txt"

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())


# with open() uses a context manager and automatically handles closing the file.


# read()
# Entire file read karta hai.

with open("data.txt", "r") as file:
    data = file.read()

print(data)



# readline()
# Ek time par ek line read karta hai.
# with open("data.txt", "r") as file:
#     line = file.readline()

# print(line)


# Agar file:-
# Hello
# Python
# World

# hai, first readline()
# Hello


# Multiple readline()
# with open("data.txt", "r") as file:
#     print(file.readline())
#     print(file.readline())


# readlines()
# Saari lines ko list mein return karta hai.
# with open("data.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

# Example output:-
# ['Hello\n', 'Python\n', 'World\n']


# File ko Loop se Read karna
# Ye clean approach hai:-
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# .strip() extra newline/whitespace remove karta hai.



# Write Mode — w
# with open("data.txt", "w") as file:
#     file.write("Hello Python")


# Agar file exist nahi karti:
# Python
#  ↓
# creates file

# Agar file already exist karti hai, old content overwrite ho jayega.
# ⚠️ Very important.

# Suppose existing:-
# Hello
# Python
# World

# # Then:-
# with open("data.txt", "w") as file:
#     file.write("New Content")

# Result:-
# New Content
# Old data gone.



# Append Mode — a
# Existing content preserve karke end mein data add karna:
# with open("data.txt", "a") as file:
#     file.write("\nNew Line")

# 🧠 Remember
# w → Replace
# a → Add


# write() vs writelines()
# write()
# with open("data.txt", "w") as file:
#     file.write("Hello")


# writelines()
# Multiple strings:-

# lines = [
#     "Python\n",
#     "JavaScript\n",
#     "React\n"
# ]

# with open("data.txt", "w") as file:
#     file.writelines(lines)



# Creating a File — x
# with open("new_file.txt", "x") as file:
#     file.write("This is a new file.")


# x ka meaning:-
# Create new file.
# Agar file already exist karti hai, error aa sakta hai.




# File Existence Check
# Python mein os module use kar sakte ho:
# import os

# if os.path.exists("data.txt"):
#     print("File exists")
# else:
#     print("File does not exist")



# Delete File
# import os
# os.remove("data.txt")

# Safe version:-
# import os

# if os.path.exists("data.txt"):
#     os.remove("data.txt")
#     print("File deleted")
# else:
#     print("File not found")



# File Path
# Same folder:-
# open("data.txt")

# Subfolder:-
# open("files/data.txt")

# Windows absolute path example:-
# open(r"C:\Users\Shahrukh\Desktop\data.txt")
# r yahan raw string ke liye h.


# Encoding
# Text files ke saath encoding explicitly specify karna good practice hai:
# with open("data.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# Writing:-
# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write("Hello Python")








