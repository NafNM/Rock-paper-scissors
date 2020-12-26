import random
# understand random module, ai generated response

def begin():
    # ask for name and gather users input, do they want to play? (Yes/No)
    name = input("Hello there! What is your name: ")
    userinput = input(f"Hello {name}, do you want to play rock, paper, scissors? (Yes/No): ")

    
    # if the response yes is provided, "userinput.upper", means that capitalisation is not considered.
    if userinput.upper() == "YES":
        game(name)
    else:
        print(f"Thanks for playing {name}.")
        againinput = input(f"Do you want to play again {name}? (Yes/No):")

    # repeats game process if the user desires
    if againinput.lower() == "yes":
        game(name)
    else:
        print(f"Thanks for playing {name}!")

# define game with the different scenarios in Rock, Paper, Scissors      
def game(name):
    ailist = ["Rock", "Paper", "Scissors"]
    ai = random.choice(ailist)
    userguess = input("Rock, Paper or Scissors?: ")
    userguess = userguess.lower() 
    ai = ai.lower()
    if userguess == ai:
        print("Wow, it was a tie!")
        print(f"The computer's guess was {ai}") 
    elif userguess == "paper" and ai == "rock":
        print(f"You won!")
        print(f"The computer's guess was {ai}")   
    elif userguess == "rock" and ai == "scissors":
        print(f"You won!")  
        print(f"The computer's guess was {ai}")     
    elif userguess == "scissors" and ai == "paper":
        print(f"You won!")  
        print(f"The computer's guess was {ai}")    
    else:
        print(f"Better luck next time, {name}!") 
        print(f"The computer's guess was {ai}")      
    
    again = input(f"Do you want to play again {name}? (Yes/No):")

    if again.upper() == "YES":
        game(name)
    else:
        print(f"Thanks for playing {name}!")

begin()


