## Error Handling in Python
## Errors can be handled gracefully using try, except, else, and finally blocks.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
else:
    print(f"Result is: {result}")
finally:
    print("This block always runs.")
