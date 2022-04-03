import os
import sys
import random

substances = ["rock", "scissors", "paper"]
computer_wins = 0
player_wins = 0
ROUNDS = 5


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def screen_drop(substance):
    if player == "quit":
        thank_you()
        print("Let's Start Again!")
        restart()
    if substance != "rock" and substance != "scissors" and substance != "paper":
        print("not acceptable\n")
        print_round()
        make_choices()
        assess_choices()
    else:
        thank_you()


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


def thank_you():
    print("Thank you\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# ROCK = 1
# SCISSORS = 2
# PAPER = 3

while computer_wins < ROUNDS and player_wins < ROUNDS:
    print_round()
    make_choices()
    assess_choices()
else:
    if winner == 1:
        print("YOU WON\n")
    else:
        print(f"THE COMPUTER WON\n")
restart()
