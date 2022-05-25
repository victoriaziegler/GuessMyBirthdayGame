from random import randint

name = input("Hi! What is your name? ")

for guess_number in range(1,6):
    month = randint(1, 12)
    year = randint(1924, 2004)

    print("Guess", guess_number, ":", name, "were you born in ", month, "/", year, "?")

    guess = input("yes or no? ")

    if guess == "yes":
        print("I knew it!")
        exit()
    elif guess_number == 5:
        print("I have other things to do. Good bye.")
    else:
        print("Drat! Lemme try again!")
    
    

    

