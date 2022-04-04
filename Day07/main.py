# The Hangman Game

import os
import random
from word_list import word_list
from hangman_art import stages, logo

print(logo)

#Randomly choose a word from word list
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

# Initialize a list with blanks equal to the length of chosen word
display = ['_']*len(chosen_word)

#Let the game begin
while not end_of_game:
    print(display)
    user_guess = input("Guess an alphabet: ").lower()
    os.system('clear')

    #Check if the user has already guessed the letter
    if user_guess in display:
        print(f"You've already guessed {user_guess} ")

    #Check if guessed letter s correct
    for i in range(len(chosen_word)):
        if(user_guess==chosen_word[i]):
            display[i] = user_guess

    #If guessed letter is incorrect
    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, It's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    
    #When user have guessed all the letters
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

    print(stages[lives])
    

    
    




