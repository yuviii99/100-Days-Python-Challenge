import random
from art import logo
print(logo + '\n')
print("Welcome to the number guessing game!")
print("I am thinking about a number between 1 and 100!")
print("I dare you to guess the number")
number = random.randint(1,100)

def play_game(level):
    game_over = False
    if level == 'easy':
        no_guess = 10
    else:
        no_guess = 5
    print(f"You have chosen the {level} level. You have {no_guess} attempts now!")
    user_input = int(input("Guess the number: "))
    while not game_over:
        if user_input == number:
            print("Great! You got the right number")
            game_over = True
        elif user_input > number:
            print("That's high")
            no_guess -= 1
            print(f"You have {no_guess} attempts left")
            user_input = int(input("Guess again: "))
        elif user_input < number:
            print("That's low!")
            no_guess -= 1
            print(f"You have {no_guess} attempts left!")
            user_input = int(input("Make a guess: "))
        if no_guess==1:
            game_over = True
            print("You have no attempts left, You Lost!")
            print(f"The number was {number}")
            break
    return

difficulty = input("Which level of difficulty would you like to face? 'easy' or 'hard'? ")
play_game(difficulty)