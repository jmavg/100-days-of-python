from random import randint

print("time to guess a number between 0 and 100")

if input("Difficulty? Easy or Hard ").lower() == "easy":
    lives = 10
else:
    lives = 5


NUMBA = randint(0,100)
game_over = False

def check(answer) -> str:
    global game_over

    if answer < NUMBA:
        print("Too low")
        return "low"

    elif answer > NUMBA:
        print("Too high")
        return "high"

    else:
        print("You got it!")
        game_over = True
        return "equal"

while game_over == False:

    print(f"You have {lives} lives")
    to_check = int(input("What's your guess? "))
    result = check(to_check)

    if result == "low" or result == "high":
        if lives > 1:
            lives -= 1

        else:
            print("Game over")
            game_over = True
