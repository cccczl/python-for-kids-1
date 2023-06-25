light_on = None

is_dark = input("Is it dark? [y/n]: ") == 'y'
is_sleepy = input("Are you sleepy? [y/n]: ") == 'y'
if is_dark and not is_sleepy:
    light_on = True
    print("Switching on the light!")
else:
    light_on = False
    print("Switching off the light!")
