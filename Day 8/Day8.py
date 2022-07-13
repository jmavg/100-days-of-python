from art import logo

print(logo)
restart = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    #Ceasar fonc
    def ceasar(input, move, mode):
        new_word = ""
        if mode == "decode":
                move *= -1

        for l in input:
            if l in alphabet:
                index = alphabet.index(l)
                new_index = index + move
                if new_index < 26:
                    new_word += alphabet[new_index]
                else:
                    new_word += alphabet[new_index-26]
            else:
                new_word += l
        print(new_word)

    ceasar(text,shift,direction)

    question = input("restart? yes or no")
    if question == "no":
        restart = False