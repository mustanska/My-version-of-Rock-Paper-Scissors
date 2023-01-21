from random import randint

options = ["Rock", "Paper", "Scissors"]

player_move = input("Press [r] to choose Rock, [p] to choose Paper or [s] to choose Scissors:")

if player_move == "r":
    player_move = options[0]
elif player_move == "p":
    player_move = options[1]
elif player_move == "s":
    player_move = options[2]
else:
    print("Invalid Input. Run the game and try again.")
    exit()

print(f"You choose {player_move}.")

computer_random_number = randint(0, 2)
computer_move = options[computer_random_number]
print(f"Computer choose {computer_move}.")

if (player_move == options[0] and computer_move == options[2]) or \
    (player_move == options[1] and computer_move == options[0]) or \
    (player_move == options[2] and computer_move == options[1]):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
