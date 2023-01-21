from random import randint
from colorama import Fore

options = ["Rock", "Paper", "Scissors"]

while True:
    player_move = input("Press [r] to choose Rock, [p] to choose Paper or [s] to choose Scissors:")

    if player_move == "r":
        player_move = options[0]
    elif player_move == "p":
        player_move = options[1]
    elif player_move == "s":
        player_move = options[2]
    else:
        print("Invalid Input.")
        continue

    print(f"You choose {player_move}.")

    computer_random_number = randint(0, 2)
    computer_move = options[computer_random_number]
    print(f"Computer choose {computer_move}.")

    if (player_move == options[0] and computer_move == options[2]) or \
            (player_move == options[1] and computer_move == options[0]) or \
            (player_move == options[2] and computer_move == options[1]):
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        print(Fore.BLUE + "Draw!")
    else:
        print(Fore.RED + "You lose!")

    restart = input(Fore.BLACK + "Do you want to restart? Press [y] or [n]:")

    if restart == "y":
        continue
    elif restart == "n":
        print("Bye.")
        break
    else:
        print("Invalid Input.")
        break
