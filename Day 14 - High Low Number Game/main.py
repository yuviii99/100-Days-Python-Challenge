#Higher Lower Game

import random
import os
from game_data import data
from art import logo, vs

def get_random_account():
    '''Get data from a random account'''
    return random.choice(data)

def format_data(account):
    '''Format information about accountable into a printable statement'''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    '''Check followers against user's guess and return whether they got it right or not'''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print(logo)
    score = 0
    game_continue = True
    a_account = get_random_account()
    b_account = get_random_account()

    while game_continue:
        a_account = b_account
        b_account = get_random_account()

        #In case when both gets same accounts randomly
        while a_account == b_account:
            b_account = get_random_account()

        print(f"Compare A: {format_data(a_account)}")
        print(vs)
        print(f"Compare B: {format_data(b_account)}")

        guess = input("Guess who has more followers, 'A' or 'B'?").lower()
        a_followers_count = a_account["follower_count"]
        b_followers_count = b_account["follower_count"]
        is_correct = check_answer(guess, a_followers_count, b_followers_count)

        os.system('clear')
        if is_correct:
            score+=1
            print(f"You're right, current score: {score}")
        else:
            game_continue = False
            print(f"Sorry you're wrong, final score: {score}")

game()