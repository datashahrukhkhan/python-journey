# *args vs **kwargs

# This is very important.
'''
*args
   ↓
Multiple positional arguments
   ↓
Tuple
**kwargs
   ↓
Multiple keyword arguments
   ↓
Dictionary

'''

# Memory trick
# *args   → tuple
# **kwargs → dictionary



# *args + **kwargs
# You can also use both:-
def student(*skills, **details):
    print("Skills:", skills)
    print("Details:", details)

student(
    "Python",
    "React",
    name="Shahrukh",
    age=21
)













