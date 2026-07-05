## Dictionaries in Python
## A dictionary stores data as key-value pairs using keys and values.

student = {"name": "Younus", "age": 18, "course": "Python"}

print("Student Dictionary:", student)
print("Student Name:", student["name"])

# Adding a new key-value pair
student["city"] = "Lahore"
print("Updated Dictionary:", student)

# Removing a value from the dictionary
student.pop("age")
print("After Removing Age:", student)

print("Keys:", student.keys())
print("Values:", student.values())
