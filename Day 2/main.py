#Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? \n$"))    #bill amount
tip = int(input("How much tip would you like to give?\n"))  #tip percentage
people = int(input("How many people to split the bill?\n"))     #number of people
amount_per_person = (bill/people) * (1 + tip/100)
print(f"Total amount payable per person is {amount_per_person}")