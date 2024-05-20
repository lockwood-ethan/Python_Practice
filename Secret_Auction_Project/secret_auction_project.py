import os
from secret_auction_art import logo

def add_new_bidders(add_one='yes', bidder_dict={}):
    #get name and bid inputs, add as key and value into bidder_dict
    while add_one == 'yes':
        print(logo)
        bidder_name = input("What is your name? ")
        os.system('cls')
        print(logo)
        bidder_bid = int(input("What is your bid? "))
        bidder_dict[bidder_name] = bidder_bid
        os.system('cls')
        print(logo)
        add_one = input("Are there any other bidders? Type 'yes' or 'no ")
        os.system('cls')
    return bidder_dict
    
bidder_dict = add_new_bidders()

#Repeat bidding if highest bidders are tied
for bidder in bidder_dict:
    if bidder != max(bidder_dict):
        if bidder_dict[bidder] == max(bidder_dict.values()):
            print("The highest bidders are tied, please bid again") 
            bidder_dict = add_new_bidders(bidder_dict={}) #TODO Fix bug, wrong key is output with max value after add_new_bidders function runs again
            break

print(logo)
print(f"The highest bidder is: {max(bidder_dict)} ${max(bidder_dict.values())}")

    