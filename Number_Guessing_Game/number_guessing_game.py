import random
from number_guessing_art import logo
number = random.choice(range(1, 101))

def stay_in_your_lane():
    global attempts
    attempts -= 1
    print("Stayin within the range. OR ELSE!")

def too_high():
    global attempts
    attempts -= 1
    print("Too high.")

def too_low():
    global attempts
    attempts -= 1
    print("Too low.")

def guess_again():
    global guess
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Guess again: "))
    return guess

def guessing_game():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    global attempts
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("You may only choose 'easy' or 'hard")
        print("Try again.")
        guessing_game()

print(logo)    
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guessing_game()
print(number)
print(f"You have {attempts} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))
while attempts > 0:
    if guess > number and guess <= 100:
        too_high()
        if attempts > 0:
            guess_again()
    elif guess < number and guess >= 1:
        too_low()
        if attempts > 0:
            guess_again()
    elif guess == number:
        print(f"You got it! The answer was {number}")
        break
    else:
        stay_in_your_lane()
        if attempts > 0:
            guess_again()
else:
    print(f"You've run out of guesses, you lose. The answer was {number}")