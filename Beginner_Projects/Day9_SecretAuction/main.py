import logo
import os

#region Main
print(logo.logo)
print("\nWelcome to the Secret Auction")

auction_values = {}

while True:
    highest_bid    = 0
    highest_bidder = "No one"

    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    auction_values[bidder_name] = bid_amount
    
    os.system('cls')

    other_bidders = input("Are there any other bidders? (Type 'yes' or 'no')\n")
    
    os.system('cls')
    
    if other_bidders == "no":
        break

for bidder in auction_values:
    if auction_values[bidder] > highest_bid:
        highest_bid = auction_values[bidder]
        highest_bidder = bidder

print(f"The highest bidder is {highest_bidder} at a bid of ${highest_bid}")

#endregion Main