from game_data import data
from art import vs, logo
import random
import os


def get_random_account():
    """get a random account from the data list"""
    return random.choice(data)


def format_display_message(account):
    """Format the display message with the given account details."""
    name = account["name"]
    description = account["description"]
    city = account["country"]

    return f"{name}, a {description} from {city}"


def check_guess(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        print("---------------------------------")
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_display_message(account_a)}.")
        print(vs)
        print(f"Against B: {format_display_message(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_guess(guess, a_follower_count, b_follower_count)

        os.system("clear")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
