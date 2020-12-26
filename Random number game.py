# Random Number Guesser
import random

# create function for game
def game():
    # computer and user input
    number = int(random.randint(0, 5))
    user = int(input("Enter your guess from 0 - 5: "))

    if user == number:
        print("You won!")
    else:
        if user > number:
            print("The actual number is a bit smaller!")
        else:
            print("The actual number is a bit larger!")

    # while loop to rerun the game function if the users input is incorrect
    while user != number:
        game()

    
game()    



