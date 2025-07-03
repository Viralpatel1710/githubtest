import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print(" Welcome to Guess the Number!")
    print("I have selected a number between 1 and 100.")
    
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print(" Too low! Try again.")
            elif guess > number_to_guess:
                print(" Too high! Try again.")
            else:
                print(f" Correct! You guessed it in {attempts} tries.")
        except ValueError:
            print(" Please enter a valid number.")

# Run the game
guess_the_number()