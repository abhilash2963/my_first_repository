import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        # Get user input
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                guessed = True
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
number_guessing_game()
