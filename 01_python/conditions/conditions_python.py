## Conditionals in python
## Conditional statements are used to perform different actions based on different conditions.

## In Python, we use the following conditional statements:

## 1. if statement
## 2. if...else statement
## 3. if...elif...else statement

## 1. if statement

name : str = "Younus"

if name == "Younus":
    print(f"Hello, {name}!")

## 2. if...else statement

a : int = 5
b : int = 10

if a > b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{a} is not greater than {b}.")

## 3. if...elif...else statement

c : int = 15
d : int = 20

if c != d:
    print(f"{c} is not equal to {d}.")
elif c == d:
    print(f"{c} is equal to {d}.")
else:
    print(f"{c} is less than {d}.")

