# Positional Arguments:-
# Arguments position ke according assign hote hain.

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Shahrukh", 21)


# Output:-
# Name: Shahrukh
# Age: 21

# Python internally:-
# name = "Shahrukh"
# age  = 21

# ⚠️ Order matters
student(21, "Shahrukh")

# Ab:-
# name = 21
# age = "Shahrukh"

# Python error nahi karega necessarily, but logic wrong ho jayega.
















