from art import logo, vs
from game_data import data
import random
import os

score = 0
game_over = False
good_choice = True

def generate_option() -> dict:

    option = data[random.randint(0,len(data)-1)]

    return option

def compare_followers(a: dict,b: dict) -> bool:

    if  a['follower_count'] > b['follower_count']:
        return True
    else:
        return False

option_a = generate_option()

def generate_option_b() -> dict:
    global option_a

    option_b = generate_option()

    while option_b == option_a:

        option_b = generate_option()

    return option_b

option_b = generate_option_b()

while game_over == False:

    print(logo)
    if score > 0:
        print(f"You're right! Current score is {score}")
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    choice = option_a if input("Who has more followers? Type A or B: ") == "A" else option_b
    good_choice = compare_followers(choice,option_b) if choice == option_a else compare_followers(choice,option_a)

    if good_choice:
        score += 1
        option_a = choice
        option_b = generate_option_b()
    else:
        game_over = True
    os.system("cls")


print(logo + f"\nSorry, that's wrong. Final score: {score}")
