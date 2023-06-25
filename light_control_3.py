def ask_user(prompt):
    return input(f"{prompt} [y/n]: ") == 'y'

light_on = None
is_dark = ask_user("Is it dark?")
is_sleepy = ask_user("Are you sleepy?")

if is_dark and not is_sleepy:
    light_on = True
    print("Switching on the light!")
else:
    light_on = False
    print("Switching off the light!")
