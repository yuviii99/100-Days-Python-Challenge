print("*************************************************************************************************")
print("*                             Welcome to the Treasure Island                                    *")
print("*                                   Find the Treasure                                           *")
print("*************************************************************************************************")
print("\n\n")
action = input("Would you like to go left or right?\n")
action = action.lower()
if action == "left":
    action = input("Would you like to swim or wait for the boat?\n")
    action = action.lower()
    if action == "wait":
        print("Great you've come this far! Only one last challenge to go!\n")
        action = input("Which door would you like to open, Red, Yellow or Blue?\n")
        action = action.lower()
        if action == "yellow":
            print("CONGRATULATIONS! You've found the treasure\n")
        else:
            print("Sorry you lost the game!")
    else:
        print("Oops! You got eaten by alligators while swimming! Better luck next time!")
else:
    print("Oops! Looks like you went the wrong way. Better luck next time!")
