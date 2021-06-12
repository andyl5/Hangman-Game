import os
import random
# import the word_list into this file
from hangman_words import word_list
# import the stages and logo art into this file
from hangman_art import stages, logo

end_of_game = False
lives = len(stages) - 1

print(logo)
display = []
# list of characters the user chooses
guessed_letters = []
# chooses a random word
chosen_word = random.choice(word_list)

# makes the dashses you see in game
for i in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    # guessed_letters.append(guess)
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = chosen_word[position]

    if guess == chosen_word[position] or guess in chosen_word:
        if guess in guessed_letters:
            print(f"You already guessed {guess}.")


    print(*display)
    if guess not in chosen_word:
        if guess in guessed_letters:
            print(f"You already guessed {guess}.")
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

    print (stages[lives])
    guessed_letters.append(guess)
    # determines whether you win or lose
    if "_" not in display :
        end_of_game = True
        print("You Win!")
    elif lives == 0:
        end_of_game = True
        print("You Lose.")
