from art import logo
import os

print(logo)
participants = {}
is_bid_active = True


def higher_bider(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        if bids[bid] > highest_bid:
            highest_bid = bids[bid]
            winner = bid

    print(f"The winner is {winner} with ${highest_bid}")


while is_bid_active:
    name = input("What's your name?: ")
    bid = float(input("What is your bid?: $"))
    participants[name] = bid
    keep_playing = input("Is there other person who wants to bid? yes or no: ")

    if keep_playing == "yes":
        os.system("clear")
    elif keep_playing == "no":
        is_bid_active = False
    else:
        print("Invalid Input! Please answer with 'yes' or 'no'.")

higher_bider(participants)
