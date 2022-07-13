choice1 = input("left or right?").lower()

if choice1 == "left":
    choice2 = input("swim or wait?").lower()
    if choice2 == "wait":
        choice3 = input("which color? Red, Blue Yellow").lower()
        if choice3 == "yellow":
            print("u did it yayy")
        else:
            print("u dead")
    else:
        print("u dead")
else:
 print("u dead")