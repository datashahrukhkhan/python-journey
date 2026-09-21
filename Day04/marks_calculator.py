# Day 4 - Mini Project
# Marks Calculator

aws = float(input("Enter AWS marks: "))
python = float(input("Enter Python marks: "))
it_laws = float(input("Enter IT Laws marks: "))
sdlc = float(input("Enter SDLc marks: "))
evs = float(input("Enter EVS marks: "))
github = float(input("Enter GitHub marks: "))

total = aws + python + it_laws + sdlc + evs + github
percentage = total / 6

print("\n--- Result ---")

print("Total Marks:", total)
print("Percentage:", percentage)