from random import randint


def print_game_title():
    print("------------------------------------------")
    print("----- Let's Play Paper Rock Scissors -----")
    print("------------------------------------------")


rand_num = randint(1, 3)

if rand_num == 1:
    comp_choice = "rock"
elif rand_num == 2:
    comp_choice = "scissors"
elif rand_num == 3:
    comp_choice = "paper"

print_game_title()
player = input("Player choose one [paper] [rock] [scissors] ").lower()

if player == comp_choice:
    print(f"It Is A Draw! Computer chose {comp_choice}")
elif player == "rock":
    if comp_choice == "scissors":
        print(f"Player One Wins! Computer chose {comp_choice}")
    elif comp_choice == "paper":
        print(f"Computer Wins! Computer chose {comp_choice}")
elif player == "paper":
    if comp_choice == "rock":
        print(f"Player One Wins! Computer chose {comp_choice}")
    elif comp_choice == "scissors":
        print(f"Computer Wins! Computer chose {comp_choice}")
elif player == "scissors":
    if comp_choice == "paper":
        print(f"Player One Wins! Computer chose {comp_choice}")
    elif comp_choice == "rock":
        print(f"Computer Wins! Computer chose {comp_choice}")
else:
    print("Something Went Wrong!")
