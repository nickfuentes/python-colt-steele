# ask for age
# could set int() here to just to take in int's
user_age = input("How old are you? ")

if user_age != "":
    # 18-21 wristband
    if int(user_age) >= 21:
        print("You are older than 21 go ahead!")
    # 21+ drink, normal entry
    elif int(user_age) >= 18:
        print("You need a wristband to enter!")
    # too young, sorry
    else:
        print("Sorry you are too young you can not enter.")
else:
    print("You need to enter an age!")
