# Combining Arguments
# You can combine different types.

def student(name, age=21, *skills):
    print(name)
    print(age)
    print(skills)

student(
    "Shahrukh",
    21,
    "Python",
    "React",
    "AWS"
)