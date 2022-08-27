from secrets import choice
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = []
options.append(rock)
options.append(paper)
options.append(scissors)


user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice > 2:
    print("Error! Insert a valid option")
else:
    print("Your choice: ")
    print(options[user_choice])

    cpu_choice = random.randint(0, 2)
    print("Computer choice: ")
    print(options[cpu_choice])

    if user_choice == 2 and cpu_choice == 0:
        print("You lose!")
    elif user_choice == 0 and cpu_choice == 2:
        print("You win!")
    elif user_choice > cpu_choice:
        print("You win!")
    elif cpu_choice > user_choice:
        print("You lose!")
    elif user_choice == cpu_choice:
        print("It's a tie!")
