import random

def guess_number():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 20. Can you guess it?")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 20:
                raise ValueError("Your guess must be between 1 and 20.")

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError as ve:
            print(ve)



if __name__ == "__main__":
    guess_number()