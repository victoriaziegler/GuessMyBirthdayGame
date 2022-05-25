from random import randint

name = input("Hi! What is your name?")

# Guess 1

guess_number = 1
month = randint(1, 12)
year = randint(1924, 2004)

print("Guess", guess_number, ": ", name, "were you born in ", month, " / ", year, "?")
guess = input("yes or no?")

if guess == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")
    

# Guess 2

guess_number = 2
month = randint(1, 12)
year = randint(1924, 2004)

print("Guess", guess_number, ": ", name, "were you born in ", month, " / ", year, "?")
guess = input("yes or no?")

if guess == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")
    

# Guess 3

guess_number = 3
month = randint(1, 12)
year = randint(1924, 2004)

print("Guess", guess_number, ": ", name, "were you born in ", month, " / ", year, "?")
guess = input("yes or no?")

if guess == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")
 

# Guess 4

guess_number = 4
month = randint(1, 12)
year = randint(1924, 2004)

print("Guess", guess_number, ": ", name, "were you born in ", month, " / ", year, "?")
guess = input("yes or no?")

if guess == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")
    

# Guess 5

guess_number = 5
month = randint(1, 12)
year = randint(1924, 2004)

print("Guess", guess_number, ": ", name, "were you born in ", month, " / ", year, "?")
guess = input("yes or no?")

if guess == "yes":
    print("I knew it!")
    exit()

else:
    print("I have other things to do. Good bye.")
    exit()