import random
from art import logo

print(logo)
print("Welcome to the guessing name")
print("I'm thingin of a number between 1 and 100,")

tries = 0
dificult = input("Choose the dificult of the game. Type hard or easy: ").lower()
number_to_guess = random.randint(1, 100)

if dificult == "easy":
    tries = 10
elif dificult == "hard":
    tries = 5


while tries > 0:
    print("-----------------------")
    print(f"You have {tries} attemps remaining to guess the number")
    guess = int(input("Type a number between 1 and 100: "))

    if guess == number_to_guess:
        print("----------You win----------")
        tries = 0
    elif guess < number_to_guess:
        print("Too low, try again")
    elif guess > number_to_guess:
        print("Too high, try again")
    else:
        print("type a valid option")

    tries -= 1
    if tries == 0:
        print("----------You lose----------")


# TODO: refactor all this project using functions
