student = {
    "name": "Shahrukh",
    "age": 22
}

try:
    print(student["marks"])

except KeyError:
    print("Marks key does not exist.")