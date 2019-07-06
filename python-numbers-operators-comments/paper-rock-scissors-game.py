def print_game_title():
    print("------------------------------------------")
    print("----- Let's Play Paper Rock Scissors -----")
    print("------------------------------------------")


def do_not_cheat():
    for index in range(30):
        print("***** DO NOT CHEAT *****")


#user_input = input("Would you like to play? yes = [y] no = [n] ")
print_game_title()
player_one = input("Player one enter [paper] [rock] [scissors] ")
do_not_cheat()
player_two = input("Player one enter [paper] [rock] [scissors] ")
if player_one == player_two:
    print("It Is A Draw!")
elif player_one == "rock":
    if player_two == "scissors":
        print("Player One Wins!")
    elif player_two == "paper":
        print("Player Two Wins!")
elif player_one == "paper":
    if player_two == "rock":
        print("Player One Wins!")
    elif player_two == "scissors":
        print("Player Two Wins!")
elif player_one == "scissors":
    if player_two == "paper":
        print("Player One Wins!")
    elif player_two == "rock":
        print("Player Two Wins!")
else:
    print("Something Went Wrong!")
