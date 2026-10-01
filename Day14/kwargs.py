# **kwargs — Multiple Keyword Arguments
# **kwargs allows multiple keyword arguments.

def student_info(**details):
    print(details)

student_info(
    name="Shahrukh",
    age=22,
    course="BCA"
)

# Important:-
# **kwargs becomes a dictionary.

print("\n")

# Loop Through **kwargs

def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(
    name="Soyab",
    age=21,
    course="MCA"
)










