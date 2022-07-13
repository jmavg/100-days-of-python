from art import logo

def add(n1,n2):
  return n1+n2

def suc(n1,n2):
  return n1-n2

def mult(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2


operations = {"+":add, "-":suc, "*":mult, "/":div}

def calculator():
  resume = True
  print(logo)
  number1 = float(input("What\'s the first number? "))

  for key in operations:
    print(key)


  while resume:

    choice = input("Choose an operator ")
    number2 = float(input("What\'s the second number? "))

    result = operations[choice](number1,number2)

    print(f"{number1} {choice} {number2} = {result} ")

    if input(f"Continue with {result} ? ") == "n":
      resume = False
      calculator()
    else:
      number1 = result

calculator()
