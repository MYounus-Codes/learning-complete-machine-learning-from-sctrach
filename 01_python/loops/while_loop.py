## While Loop in Python

## A while loop is used to execute a block of code repeatedly as long as a given condition is true.

print("Using a while loop to print numbers from 0 to 4:\n")

i = 0
while i < 5:
    print(f"Current value of i: {i}")
    i += 1  # Incrementing i to avoid infinite loop


print("\nUsing a while loop to print even numbers from 0 to 10:\n")

i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

while True:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.\n")
        break  # Exiting the loop when user types 'exit'
    else:
        print(f"You entered: {user_input}\n")
