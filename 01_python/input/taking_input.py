## Taking Input from the User using the built-in input() function of Python

name = input("Enter your name: ")
age = input("Enter your age: ")

if (name == "Younus") and (age == "18"):
    print("Hello Boss! You are 18 years old.")
else:
    print(f"Dear {name}! You are {age} years old.")

## Taking Input from the User of a specific data type using the built-in input() function of Python

city = str(input("Enter your city: "))
print(f"You live in {city}.") 