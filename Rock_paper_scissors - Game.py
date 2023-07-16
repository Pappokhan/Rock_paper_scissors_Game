import random

def game(player, Ai):
    if player == Ai:
        return "It's a tie!"
    elif (player == 'rock' and Ai == 'scissors'):
        return "Congratulations.. You win!"
    elif (player == 'paper' and Ai == 'rock'):
        return "Congratulations.. You win!"
    elif (player == 'scissors' and Ai == 'paper'):
        return "Congratulations.. You win!"
    else:
        return "You loss.. Ai wins!"
        
while True:
    choices = ['rock', 'paper', 'scissors']
    print("--Welcome to game!--")
    print() 
    player = input("You chose (rock, paper, or scissors): ")
    
    if player not in choices:
        print("Invalid choice...")
    else:
        Ai = random.choice(choices)
        print(f"AI chose----------------------------: {Ai}")
        print(game(player, Ai))

    print()   
    next = input("Do you want to play again? (yes/no): ")
    if next == "no":
        break
    else:
        pass