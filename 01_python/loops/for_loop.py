## For Loop in Python
## The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.

## Basic For Loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

## Using range() function

for i in range(5):
    print(i)

## Nested For Loops

for i in range(3):
    for j in range(3): ## Nested loop to iterate over a range of numbers
        print(f"({i}, {j})")


## Problem: Write a for loop that prints the square of numbers from 1 to 10.

for i in range(1, 11):
    print(f"The square of {i} is: {i ** 2}")