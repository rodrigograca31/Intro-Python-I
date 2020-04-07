import random

print("Lets play a game?\n")

print("1. Rock, \n2. Paper, \n3. Scissors\n")

option = 99

while option != 0:
    option = int(input("Whats gonna be? "))
    if option not in [1, 2, 3]:
        print("Invalid option")
        continue

    pc_option = random.randint(a=1, b=3)

    result = abs(option - pc_option)

    if result == 0:
        print("Tie")
    elif result == 1:
        if option < pc_option:
            print("You lost")
        else:
            print("You won")
    else:
        if option > pc_option:
            print("You lost")
        else:
            print("You won")


print("The end")
