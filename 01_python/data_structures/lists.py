## Lists in Python
## Lists are one of the most versatile data structures in Python. They can hold a collection of items, which can be of different types, and they are mutable, meaning you can change their content without changing their identity.

names : list = ["Muhammad", "Anees", "Younus", "Ali", "Ahmed"]
numbers : list = [1, 2, 3, 4, 5]
mixed : list = ["Hello", 42, 3.14, True]

print("Names List:", names)
print("Numbers List:", numbers)
print("Mixed List:", mixed)

print("\nList Lengths:")
print("Length of Names List:", len(names))
print("Length of Numbers List:", len(numbers))
print("Length of Mixed List:", len(mixed))

print("\nChecking Types:")
print("Type of Names List:", type(names))
print("Type of Numbers List:", type(numbers))
print("Type of Mixed List:", type(mixed))

print("\nAccessing Elements:")
print("First name:", names[0])
print("Last number:", numbers[-1])
print("Second mixed element:", mixed[1])

print("\nModifying Lists:")
names[0] = "Mohammed"
numbers[2] = 10
mixed[3] = False

print("Modified Names List:", names)
print("Modified Numbers List:", numbers)
print("Modified Mixed List:", mixed)

print("\nList Operations:")
# Adding elements
names.append("Sara")
numbers.extend([6, 7, 8])
print("After Adding Elements:")
print("Names List:", names)
print("Numbers List:", numbers)

# Removing elements
names.remove("Ali")
numbers.pop(0)  # Removes the first element
print("After Removing Elements:")
print("Names List:", names)
print("Numbers List:", numbers)

