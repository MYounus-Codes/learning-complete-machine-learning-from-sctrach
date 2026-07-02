## Note: This code is written in Python 3.6 or later, as it uses f-strings for string formatting. 

## --------------------------------------------------------------------------------------------------------##

## Basics :
## Variables, Data Types, and Basic Operations and f-strings

## Variables and Data Types
# Variables are used to store data in Python. You can assign a value to a variable using the equals sign (=). Python has several built-in data types, including integers, floats, strings, and booleans.

## Rules of Variable Naming:
# 1. Variable names must start with a letter or an underscore (_).
# 2. Variable names can contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive (e.g., myVariable and myvariable are different variables).


## Variable Declaration and Initialization

name : str = "Alice"  # String
age : int = 30        # Integer
height : float = 5.6    # Float
is_student : bool = True  # Boolean

## Printing Variables and Their types

print("\n--- Variable Values and Types ---\n")

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")

## Basic Operations

a = 10
b = 3

# Arithmetic Operations

c = a + b  # Addition
d = a - b  # Subtraction
e = a * b  # Multiplication
f = a / b  # Division
g = a // b # Floor Division
h = a % b  # Modulus

print("\n--- Basic Operations ---\n")

print(f"Addition: {c}")
print(f"Subtraction: {d}")
print(f"Multiplication: {e}")
print(f"Division: {f}")
print(f"Floor Division: {g}")
print(f"Modulus: {h}")

## Comparison Operations

i = a > b   # Greater than
j = a < b   # Less than
k = a == b  # Equal to
l = a != b  # Not equal to

print("\n--- Comparison Operations ---\n")

print(f"Greater than: {i}")
print(f"Less than: {j}")
print(f"Equal to: {k}")
print(f"Not equal to: {l}")

## Logical Operations

m = (a > b) and (b > 0)  # Logical AND
n = (a > b) or (b < 0)   # Logical OR
o = not (a == b)         # Logical NOT

print("\n--- Logical Operations ---\n")
print(f"Logical AND: {m}")
print(f"Logical OR: {n}")
print(f"Logical NOT: {o}")

## f-strings

print("\n--- f-strings ---\n")

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}\n")