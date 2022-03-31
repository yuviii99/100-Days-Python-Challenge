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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

choice = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice>=3 or user_choice<0:
    print("Invalid Choice")
else:
    print("You Chose: \n" + choice[user_choice] + "\n")
    print("Computer Chose: \n" + choice[computer_choice] + '\n')
    if user_choice==0 and computer_choice==2:  
        print("You Win!")
    elif user_choice==2 and computer_choice==0:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice < computer_choice:
        print("You Lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")