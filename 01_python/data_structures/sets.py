## Sets in Python
## A set is an unordered collection of unique items.

numbers = {1, 2, 2, 3, 4}
print("Set of Numbers:", numbers)

# Adding and removing elements
numbers.add(5)
numbers.remove(3)
print("Updated Set:", numbers)

# Set operations
even_numbers = {2, 4, 6, 8}
print("Union:", numbers | even_numbers)
print("Intersection:", numbers & even_numbers)
print("Difference:", numbers - even_numbers)
