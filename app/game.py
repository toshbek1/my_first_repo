# THIS IS MY ROCK PAPER SCISSORS GAME

print("WELCOME TO MY GAME...")

player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")
print("USER CHOSE:", player_choice)

# todo: validation step

import random

VALID_OPTIONS = ["rock", "paper", "scissors"]

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOSE:", computer_choice)

# todo: determine the winner

print("WINNER: TODO")