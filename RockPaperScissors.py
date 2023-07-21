import random

print("----------WELCOME TO RPS!! Let the game begin!----------")
print("\t \t  To exit enter No")

RPS = ["rock", "paper", "scissors"]
RPS_Computer = random.choice(RPS)

while True:
    RPS_User = str(input("What is your choice? Rock, Paper, Scissors? ")).lower()

    if RPS_Computer == "rock" and RPS_User == "rock" or RPS_Computer == "paper" and RPS_User == "paper" \
            or RPS_Computer == "scissors" and RPS_User == "scissors":
        print("Tie!")

    elif RPS_Computer == "rock" and RPS_User == "scissors":
        print("You lose! Rock smashes Scissors")

    elif RPS_Computer == "paper" and RPS_User == "rock":
        print("You lose! Paper covers Rock")

    elif RPS_Computer == "scissors" and RPS_User == "paper":
        print("You lose! Scissors cut Paper")

    elif RPS_Computer == "scissors" and RPS_User == "rock":
        print("You win! Rock smashes Scissors")

    elif RPS_Computer == "rock" and RPS_User == "paper":
        print("You win! Paper covers Rock")

    elif RPS_Computer == "paper" and RPS_User == "scissors":
        print("You win! Scissors cut Paper")

    elif RPS_User == "no":
        print("Thank you for playing RPS :)")
        exit()

    else:
        print("That's not a valid play. Invalid option!")

