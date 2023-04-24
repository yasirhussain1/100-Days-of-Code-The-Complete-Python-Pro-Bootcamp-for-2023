from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
bids = {}

should_continue = True
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while should_continue:    
  name = input("What's your name?: ")
  price = int(input("what's your bid?: $"))
  bids[name] = price
  new_bidder = input("Are there other bidders? Type 'yes' or 'no'.\n")
  if new_bidder == "no":
    should_continue = False
    find_highest_bidder(bids)
  elif new_bidder == "yes":
    clear()
