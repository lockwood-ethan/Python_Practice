import random, os
from blackjack_art import logo

def hit_me():
    new_card = random.choice(cards)
    return new_card
def deal():
    want_to_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    os.system("cls")
    print(logo)
    global dealer_hand
    dealer_hand = []
    global player_hand
    player_hand = []
    if want_to_play == 'y':
        while  len(dealer_hand) <= 1:
            new_card = hit_me()
            dealer_hand.append(new_card)
        while  len(player_hand) <= 1:
            new_card = hit_me()
            player_hand.append(new_card)
    else:
        print("Probably better for your wallet that way, loser.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
deal()

while sum(dealer_hand) <= 17:
    new_card = hit_me()
    dealer_hand.append(new_card)
    if sum(dealer_hand) > 21 and 11 in dealer_hand:
        ace_index = dealer_hand.index(11)
        dealer_hand[ace_index] = 1

print(f'    Your cards: {player_hand}, current score: {sum(player_hand)}')
print(f'    Computer\'s first card: {dealer_hand[0]}')
another_card = input("Type 'y' to get another card, type 'n' to pass: ")
while another_card == 'y':
    new_card = hit_me()
    player_hand.append(new_card)

    if sum(player_hand) > 21 and 11 in player_hand:
        ace_index = player_hand.index(11)
        player_hand[ace_index] = 1
    elif sum(player_hand) > 21:
        print(f'You went over 21, you bust!')
        print(f'Player hand: {player_hand} Player total: {sum(player_hand)}')
        print(f'Computer hand: {dealer_hand} Computer total: {sum(dealer_hand)}')
        deal()
            
    print(f'    Your cards: {player_hand}, current score: {sum(player_hand)}')
    print(f'    Computer\'s first card: {dealer_hand[0]}')
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

if sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) < 21:
    print("Computer wins!")
    print(f'Computer hand: {dealer_hand} Computer total: {sum(dealer_hand)}')
    print(f'Player hand: {player_hand} Player total: {sum(player_hand)}')
    deal()
elif sum(dealer_hand) == sum(player_hand):
    print("It's a draw!")
    print(f'Player hand: {player_hand} Player total: {sum(player_hand)}')
    print(f'Computer hand: {dealer_hand} Computer total: {sum(dealer_hand)}')
    deal()
else:
    print("Player wins!")
    print(f'Player hand: {player_hand} Player total: {sum(player_hand)}')
    print(f'Computer hand: {dealer_hand} Computer total: {sum(dealer_hand)}')
    deal()