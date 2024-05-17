import random
import hangman_art
from hangman_words import word_list
from replit import clear

print(hangman_art.logo)

total_lives = 6
chosen_word = random.choice(word_list)
display = []
used_letters = []
for letter in chosen_word:
    display.append('_')
print("Cheater!", chosen_word)
print(f"Word: {' '.join(display)}")
guess = input("Guess a letter:").lower()
clear()
while total_lives > 0:
    print(hangman_art.logo)
    if len(guess) != 1:
        print("Guess must be exactly one character. Try again.")
        print(hangman_art.stages[total_lives])
        guess = input("Guess a letter:")
        clear()
    if guess in used_letters:
        print("You already chose that letter, try again.")
        print(hangman_art.stages[total_lives])
        guess = input("Guess a letter:")
        clear()
    else:
        if guess in chosen_word:
            num_amount = 0
            for pos, letter in enumerate(chosen_word):
                if letter == guess:
                    display[pos] = letter
                    num_amount += 1
            used_letters.append(guess)
            if '_' in display:
                print(f"{guess.capitalize()} is in the word {num_amount} times.")
                print(f"Word: {' '.join(display)}")
                print(hangman_art.stages[total_lives])
                guess = input("Guess a letter:").lower()
                clear()
            else:
                print(hangman_art.stages[total_lives])
                print(f"You win! Word: {chosen_word}")
                break
        else:
            total_lives -= 1
            if total_lives == 0:
                print(hangman_art.stages[total_lives])
                print(f"You are out of lives. You LOSE! Word: {chosen_word}")
                break
            else:
                used_letters.append(guess)
                print(f"That letter is not in the word. Lost a life. Lives left: {total_lives}")
                print(f"Word: {' '.join(display)}")
                print(hangman_art.stages[total_lives])
                guess = input("Guess a letter:").lower()
                clear()
