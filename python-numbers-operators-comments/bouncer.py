# ask for age
user_age = int(input("How old are you? "))

# 18-21 wristband
if user_age >= 18 and user_age < 21:
    print("You need a wristband to enter.")
# 21+ drink, normal entry
elif user_age >= 21:
    print("You are older than 21 go ahead!")
# too young, sorry
else:
    print("Sorry you are too young you can not enter.")
