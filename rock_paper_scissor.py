import os
import sys
import random
substances = ["rock", "scissors", "paper"]
computer_wins = 0
player_wins = 0

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def screen_drop(substance):
    if substance != "rock" and substance != "scissors" and substance != "paper":
        print("not acceptable\n")
        print_round()
        make_choices()
        assess_choices()
    else:
        print("Thank you\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def print_round():
    print(f"Current Score:\nPlayer: {player_wins} -- Computer: {computer_wins}")

def make_choices():
    global player
    global computer
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("(Enter Player 1's choice): ")
    screen_drop(player)

    print("SHOOT!")

    computer = substances[random.randint(0, 2)]
    print(f"Player 1 plays {player} and Player 2 plays {computer}")

def assess_choices():
    global winner
    global player
    global computer
    global player_wins
    global computer_wins
    winner = 0
    if player == "rock":
        if computer == "scissors":
            winner = 1
        else:
            winner = 2
    if player == "scissors":
        if computer == "paper":
            winner = 1
        else:
            winner = 2
    if player == "paper":
        if computer == "rock":
            winner = 1
        else:
            winner = 2
    if player == computer:
        print("no winner")
        winner = 0

    if winner == 1:
        print("You are this round's winner.\n")
        player_wins += 1
    elif winner == 2:
        print(f"Computer won this round.\n")
        computer_wins += 1
    winner = 0



# ROCK = 1
# SCISSORS = 2
# PAPER = 3

while computer_wins < 3 and player_wins < 3:
    print_round()
    make_choices()
    assess_choices()





else:
    if winner == 1:
        print("YOU WON\n")
    else:
        print(f"THE COMPUTER WON\n")

restart()
