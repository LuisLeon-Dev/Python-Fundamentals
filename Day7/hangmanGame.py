import random
from hangman_art import logo, stages
from hangman_words import word_list


end_of_game = False
lives = 6
chosen_word = random.choice(word_list)

print(logo)
print(chosen_word)

display = []
for _ in chosen_word:
    display.append("_")


while not end_of_game:
    guess = input("Insert a letter: ").lower()
    if guess in display:
        print(f"You've already guess {guess}")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"the letter {guess} is not in the word. You lose a life")
        if lives == 0:
            print("You Lose!")
            end_of_game = True

    print("".join(display))
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You won!")
        print("The word was:", "".join(display))
