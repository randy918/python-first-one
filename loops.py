import os
import sys
from random import randint

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def get_guess():
    global received
    received = input(starter + " ")
    if str.isdigit(received) and int(received) >= LOW and int(received) <= HIGH:
        received = int(received)
    else:
        print("Try again.")
        get_guess()

def assess_guess(received):
    if received == number:
        print("Correct!\nLet's Start Again!")
        restart()
    elif received < number:
        print("Too Low")
    elif received > number:
        print("Too High")

LOW = 1
HIGH = 10
number = randint(LOW, HIGH)
starter = f"\nGuess a number from {LOW} to {HIGH}:"

win = False

while win is False:
    get_guess()
    assess_guess(received)

restart()






