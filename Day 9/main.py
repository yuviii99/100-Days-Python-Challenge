#Secret Auction
import os
from art import logo
print(logo)

bids = {}
not_completed = True
while not_completed:
    name = input("Enter your name: ")
    bid = int(input("Enter the bid amount: $"))
    bids[name] = bid
    status = input("Are there any other bidders? Enter 'Yes' or 'No'\n").lower()
    if status=='yes':
        os.system('clear')
    else:
        not_completed = False
maxbid = 0
for name,bid in bids.items():
    if bid > maxbid:
        maxbid = bid
        bidder = name
os.system('clear')
print(f"The highest bidder is {bidder} with a bid of ${maxbid}\n")