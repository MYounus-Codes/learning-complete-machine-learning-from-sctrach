## Functions in Python
## A function is a block of code that performs a specific task and can be reused throughout the program.

## Defining a Function

def greet(name: str) -> None:
    print(f"Hello, {name}!")

## Calling a Function

greet("Younus")
greet("Ali")
greet("Ahmed") ## Now we dont have to write the same code again and again, we can just call the function with different arguments.

def add_numbers(a : int, b : int) -> int:
    return a + b

result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {result}")

## More complex function

def calculate_area(length: float, width: float) -> float:
    area = length * width
    return area

result = calculate_area(5.0, 10.0)
print(f"The area of the rectangle is: {result}")    

