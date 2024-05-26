import random
import game_data
import art
import os

def start_game():
    print(art.logo)
    return (f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']}.")

def versus():
    print(art.vs)
    return (f"Compare B: {option2['name']}, a {option2['description']}, from {option2['country']}.")

def decision():
    player_choice = input("Who has more followers? Type 'A' or 'B': ")
    return player_choice

def right_answer():
    print(art.logo)
    print(f"Correct! Current score: {current_score}")
    return (f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']}.")

def wrong_answer():
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        return False

def check_answer():
    global option1
    global option2
    global current_score
    if player_choice == 'A' and option1['follower_count'] > option2['follower_count']:
        current_score += 1
        get_new()
        return True
    elif player_choice == 'B' and option1['follower_count'] < option2['follower_count']:
        current_score += 1
        option1 = option2
        get_new()
        return True
    else:
         return wrong_answer()

def get_new():
    global option1
    global option2
    option2 = random.choice(game_data.data)
    while option1 == option2:
        option2 = random.choice(game_data.data)

current_score = 0
option1 = random.choice(game_data.data)
option2 = random.choice(game_data.data)
while option1 == option2:
    option2 = random.choice(game_data.data)
keep_going = True

print(start_game())
print(versus())
player_choice = decision()
os.system("cls")
while keep_going == True:
    keep_going = check_answer()
    if keep_going == True:
        print(right_answer())
        print(versus())
        player_choice = decision()
        os.system("cls")
