# this is the "game.py" file...
import random

print("let's play a game of rock, paper, scissors!")


# USER INPUTS

user_choice = input("please choose ('rock', 'paper', 'scissors'): ")
user_choice = user_choice.lower()

# you chose: 'rock'
print("you chose:", user_choice)

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
    print("it's a tie! you both win!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("rock beats scissors, you win!")
    else:
        print("paper beats rock, you lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("paper beats rock, you win!")
    else:
        print("scissors beats paper, you lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("scissors beats paper, you win!")
    else:
        print("rock beats scissors, you lose!")




print("thanks for playing, want to play again?")


# DISPLAY RESULTS
