import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    # Randomly generate a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        # Prompt user to input their guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if the guess is too high, too low, or correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
    
if __name__ == "__main__":
    guessing_game()
