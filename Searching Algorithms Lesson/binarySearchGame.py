# Guess the number
#This program generates a random number between 1 and 64 and
#the player has to guess it.
#The computer tells the player each time if their guess is too low or too high
#or if they have guessed it correctly

import random

print("This is a simple guessing game.")
print("I am going to think of a number between 1 and 64, and you have to guess it.")
print("I will tell you whether your guess is too high, too low or correct each time.")
print("You should be able to guess it in 6 guesses or less.")

#initialise variables
myNumber = random.randint(1,64)
guess = int(input("Please type your guess: "))
numberOfGuesses = 1

#main loop
while guess != myNumber:
    if guess > myNumber:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    guess = int(input("Guess again: "))
    numberOfGuesses = numberOfGuesses + 1

print("Correct! You took",numberOfGuesses,"guesses.\n")
input("\nPress Enter to exit.")