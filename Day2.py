total = float(input("What's the total?: $"))
tip = 1 + int(input("how much tip? 10, 12 or 15?"))/100
peeps = int(input("how many peep?"))

print(f"you'll each have to pay {round(total*tip/peeps, 2)}")