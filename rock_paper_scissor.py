import os
import sys
from random import randint



def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def screen_drop(substance):
    if substance != "rock" and substance != "scissors" and substance != "paper":
        print("not acceptable\n")
        restart()
    else:
        print("Thank you\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


substances = ["rock", "scissors", "paper"]

# ROCK = 1
# SCISSORS = 2
# PAPER = 3



print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
screen_drop(player1)


print("SHOOT!")

player2 = substances[randint(0, 2)]
print(f"Player 1 plays {player1} and Player 2 plays {player2}")

if player1 == player2:
    print("no winner")
    restart()

if player1 == "rock":
    if player2 == "scissors":
        winner = 1
    else:
        winner = 2

if player1 == "scissors":
    if player2 == "paper":
        winner = 1
    else:
        winner = 2

if player1 == "paper":
    if player2 == "rock":
        winner = 1
    else:
        winner = 2

print(f"Winner is player{winner}")

restart()
