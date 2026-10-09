# Python Packages
# Module = ek .py file
# Package = multiple modules ko organize karne wala folder


# Package kya hota hai?
# Python package ek directory/folder hota hai jisme multiple Python modules hote hain.


# Example:-

# my_project/
# │
# ├── main.py
# │
# └── calculator/
#     ├── __init__.py
#     ├── addition.py
#     ├── subtraction.py
#     └── multiplication.py


# Yahan:-

# addition.py       → Module
# subtraction.py    → Module
# multiplication.py → Module

# calculator/       → Package



from importlib.resources import Package


# Module vs Package

# Module	                Package
# Ek Python file	        Ek folder
# .py file hoti hai	        Multiple modules contain kar sakta hai
# Small reusable code	    Large code organization
# Example: math_utils.py	Example: calculator/


# Package ki zarurat kyu hai?
# Imagine tumhara project bada ho gaya:-
# project/
# ├── students.py
# ├── teachers.py
# ├── fees.py
# ├── attendance.py
# ├── exams.py
# ├── database.py
# ├── authentication.py
# ├── payments.py
# └── ...


# Sab files root folder mein hone se project messy ho sakta hai.
# Packages se:-
# project/
# │
# ├── students/
# │   ├── registration.py
# │   └── profile.py
# │
# ├── teachers/
# │   ├── profile.py
# │   └── attendance.py
# │
# ├── payments/
# │   ├── fees.py
# │   └── transactions.py
# │
# └── main.py




# PyPI kya hai?
# PyPI = Python Package Index
# Ye Python packages ka huge online repository hai.


# pip kya hai?
# pip Python packages install/manage karne ka commonly used tool hai.



# 🧠 Memory Trick
# PyPI = Package Store
# pip  = Package Installer/Manager














