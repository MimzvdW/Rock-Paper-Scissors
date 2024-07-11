import random

print("----------WELCOME TO RPS!! Let the game begin!----------")
print("\t \t  To exit enter No")

# List of possible choices for Rock, Paper, Scissors
RPS = ["rock", "paper", "scissors"]
# Computer randomly selects one choice from the list
RPS_Computer = random.choice(RPS)

# Start an infinite loop for the game
while True:
    # User input for their choice, converted to lowercase for consistency
    RPS_User = str(input("What is your choice? Rock, Paper, Scissors? ")).lower()

     # Check if it's a tie
    if RPS_Computer == "rock" and RPS_User == "rock" or RPS_Computer == "paper" and RPS_User == "paper" \
            or RPS_Computer == "scissors" and RPS_User == "scissors":
        print("Tie!")

    # Check if the user loses
    elif RPS_Computer == "rock" and RPS_User == "scissors":
        print("You lose! Rock smashes Scissors")

    elif RPS_Computer == "paper" and RPS_User == "rock":
        print("You lose! Paper covers Rock")

    elif RPS_Computer == "scissors" and RPS_User == "paper":
        print("You lose! Scissors cut Paper")

    # Check if the user wins
    elif RPS_Computer == "scissors" and RPS_User == "rock":
        print("You win! Rock smashes Scissors")

    elif RPS_Computer == "rock" and RPS_User == "paper":
        print("You win! Paper covers Rock")

    elif RPS_Computer == "paper" and RPS_User == "scissors":
        print("You win! Scissors cut Paper")

    # Check if the user wants to exit the game
    elif RPS_User == "no":
        print("Thank you for playing RPS :)")
        exit()

    # Handle invalid input
    else:
        print("That's not a valid play. Invalid option!")

