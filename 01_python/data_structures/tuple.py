## Tuples in Python
## A tuple is similar to a list, but it is immutable, meaning it cannot be changed after creation.

coordinates = (10, 20)
print("Tuple:", coordinates)
print("First Value:", coordinates[0])

# Unpacking a tuple
x, y = coordinates
print(f"x = {x}, y = {y}")

# Trying to change a tuple value will raise an error
try:
    coordinates[0] = 15
except TypeError:
    print("Tuples are immutable, so values cannot be changed.")
