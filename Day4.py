import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


GUI = [rock,paper,scissors]
choice = int(input("What ya want? 0 rock, 1 paper, 2 scissors"))
NPC = random.randint(0,2)

if choice >= 0 and choice < 3:
    print(f"choir choice:\n {GUI[choice]}\n Computer\'s choice:\n {GUI[NPC]}")

    if choice == 0:
        if NPC == 0:
            print("Draw")
        elif NPC == 1:
            print("U lose")
        else:
            print("U won")
    elif choice == 1:
        if NPC == 0:
            print("U won")
        elif NPC == 1:
            print("Draw")
        else:
            print("U lose")
    else:
        if NPC == 0:
            print("U lost")
        elif NPC == 1:
            print("U won")
        else:
            print("Draw")
else:
    print("Don\'t you know how to read? it's 0, 1 or 2?!?!")
