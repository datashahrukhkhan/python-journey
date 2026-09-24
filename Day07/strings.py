# Day 7 - Strings
# Python Learning Journey



# 1. BASIC STRINGS
name = "Shahrukh"
city = "Jaipur"
course = "BCA"

print("Name:", name)
print("City:", city)
print("Course:", course)



# 2. STRING LENGTH

print("\nString Length")

print("Name length:", len(name))
print("City length:", len(city))



# 3. INDEXING


print("\nString Indexing")

language = "Python"

print("First character:", language[0])
print("Second character:", language[1])
print("Last character:", language[-1])



# 4. SLICING

# here happens to be a string slicing example, but the comment seems to be incomplete. The code below demonstrates string slicing in Python.
print("\nString Slicing")

print(language[0:3])
print(language[2:6])
print(language[:4])
print(language[2:])



# 5. STRING METHODS


text = "python programming"

print("\nString Methods")

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())



# 6. STRIP


user_input = "   Shahrukh   "

print("\nStrip")

print(user_input.strip())



# 7. REPLACE


message = "I am learning Java"

print("\nReplace")

print(message.replace("Java", "Python"))



# 8. FIND


sentence = "Python is powerful"

print("\nFind")

print(sentence.find("powerful"))
print(sentence.find("Java"))


# 9. CHECKING STRING

skill = "Python"

print("\nString Checks")

print(skill.startswith("Py"))
print(skill.endswith("on"))


# 10. MEMBERSHIP

print("\nMembership")

print("Python" in "I am learning Python")
print("Java" in "I am learning Python")


# 11. STRING CONCATENATION

first_name = "Shahrukh"
last_name = "Khan"

full_name = first_name + " " + last_name

print("\nFull Name:", full_name)


# 12. F-STRING\
    
age = 21
specialization = "Cloud Computing"

print(
    f"\nMy name is {first_name} {last_name}. "
    f"I am {age} years old and I am learning {specialization}."
)