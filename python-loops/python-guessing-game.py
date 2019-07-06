import random

rand_num = random.randint(1, 10)
user_input = ""

while user_input != "n":
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < rand_num:
        print("TOO LOW!")
    elif guess > rand_num:
        print("TOO HIGH!")
    else:
        print("You Won!!!")
    user_input = input("Do you want to play again? (y/n) ")


"""user_input = ""
while user_input != "n":
    user_guess = int(input("Guess a number between 1-10: "))
    if user_guess == rand_num:
        print("You Guessed Right!!")
    else:
        print("Sorry You Guessed Wrong!")
    user_input = input("Do you want to play again? yes = [y] no  = [n]: ")"""
