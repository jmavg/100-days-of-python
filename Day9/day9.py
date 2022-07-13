from art import logo
import os

clear = lambda: os.system('cls')
cont = True
highest_bid = 0
person = ""

print(logo + "\n Welcome to the secret action thingy")
info = {}
while cont:
    name = input("What\'s your name? ")
    bid = int(input("What\' s your bid? $"))

    info[name] = bid
    more = input("Are there more people?")

    if more == "no":
        cont = False

    clear()

for peep in info:
    if info[peep] > highest_bid:
        highest_bid = info[peep]
        person = peep

print(f'The winner is {person} with a bid of ${info[person]}')