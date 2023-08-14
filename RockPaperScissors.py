import random

print("Play Rock Paper Scissors")

while(True):
    botchoice = random.choice(['r', 'p', 's'])
    playerchoice = input("Enter r for Rock, p for Paper, s for scissors. q to quit: ")
    if playerchoice == 'q':
        break
    print(f"You choose {playerchoice} and the bot choose {botchoice}")

    if playerchoice == botchoice:
        print("It's a tie!")

    if playerchoice == 'p' and botchoice == 'r' or playerchoice == 'r' and botchoice == 's' or playerchoice == 's' and botchoice == 'p':
        print("You win!")
    elif playerchoice == 'r' and botchoice == 'p' or playerchoice == 's' and botchoice == 'r' or playerchoice == 'p' and botchoice == 's':
        print("You lose!")

    
