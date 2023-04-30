from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """formats the account data into printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and return if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
#Display art 
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatable
while game_should_continue:
  # generate a random acount from the game data
  # making account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
    
  print(f"Compare A: {format_data(account_a)} ")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  # Ask user for guess
  guess = input("Who has more followers? 'A' or 'B': ").lower()
  
  # Check if the user is correct.
  ## Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
# Clear the screen
  clear()
  print(logo)
  # Give user feedback on their guess.
  # score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score is : {score}.")
    account_a = account_b
    
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong, final score {score}.")
