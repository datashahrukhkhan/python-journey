# Day 6 - Loops
# Python Learning Journey

# 1. FOR LOOP
for i in range(5):
    print(i)
    print("Hello, I'm Shahrukh Khan! \n")


# range(start, stop)
# start → included
# stop  → excluded
# 1 ≤ i < 6
for i in range(1, 6):
    print(i)


# print numbers from 1 to 10
print("\nNumbers 1 to 10")
for i in range(1, 11):
    print(i)

# print numbers from 1 to 10 in reverse order
print("\nEven Numbers")
for i in range(2, 21, 2):
    print(i)

# print numbers from 1 to 10 in reverse order
print("\nOdd Numbers")
for i in range(1, 20, 2):
    print(i)



# print 3 tables from 3 to 30
print("\n3 Tables")
for i in range(3, 31, 3):
    print(i)


# sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total = total + i

print("\nTotal:", total)


# loop through a list
skills = ["Python", "AWS", "Azure", "Git", "Linux"]

print("\nSkills:")
for skill in skills:
    print( skill)


# if-else +  for loop
numbers = [10, 15, 20, 25, 30]

for number in numbers:

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# break statement
for i in range(1, 11):

    if i == 6:
        break

    print(i)

# continue statement
for i in range(1, 6):

    if i == 3:
        continue

    print(i)


# nested for loop
# Outer loop
#    ↓
#  1
#  ├── Inner: 1 2 3

#  2
#  ├── Inner: 1 2 3

#  3
#  ├── Inner: 1 2 3
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)







