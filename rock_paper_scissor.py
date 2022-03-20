import os
import sys


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def is_material(substance):
    if substance != "rock" and substance != "scissors" and substance != "paper":
        print("not acceptable\n")
        restart()
    else:
        print("Thank you\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
is_material(player1)

player2 = input("(enter Player 2's choice): ")
is_material(player2)

print("SHOOT!")

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
