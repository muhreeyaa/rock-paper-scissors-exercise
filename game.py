# this is the "game.py" file...
import random

print("Let's play a game of Rock, Paper, Scissors!")


# USER INPUTS


user_choice = input("Please choose ('rock', 'paper', 'scissors'): ")
user_choice = user_choice.lower()

# you chose: 'rock'
print("You chose:", user_choice)
print(f"You chose: '{user_choice}'")

# VALIDATE USER INPUTS

valid_options = ["rock", "paper", "scissors"]

#breakpoint()

# if user_choice in valid_options:
#   # ALL THE STUFF INDENTED
#  pass
# else:
# print("OOPS INVALID, TRY AGAIN")



if user_choice not in valid_options:
    print("OOPS INVALID, TRY AGAIN")
    exit() # quit ()

# COMPUTER CHOICE


#import random

computer_choice = random.choice(valid_options)
print("computer chose:", computer_choice)


# adapted from code shared in slack
if user_choice == computer_choice:
    print("it's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("rock beats scissors! woo, you won!")
    else:
        print("paper beats rock, you lost :(")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("paper beats rock! woo, you won!")
    else:
        print("scissors beats paper, you lost :(")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("scissors beats paper! woo, you won!")
    else:
        print("rock beats scissors, you lost :(")


# DETERMINE THE WINNER


# DISPLAY RESULTS

# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!