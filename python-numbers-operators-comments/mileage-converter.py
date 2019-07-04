user_input = float(input("How many kilometers did you run today? "))


def convert_kilo_to_miles():
    miles = round(user_input / 1.60934, 2)
    return miles


miles = convert_kilo_to_miles()

print(
    f"Okay you said you ran {user_input}kms. That is {miles} miles! Great Job!")
