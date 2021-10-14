def game():
    import random

    print("\nROCK PAPER SCISSORS\n")

    print("\nWeapon to choose :\n")

    print("1. ROCK")
    print("2. PAPER")
    print("3. SCISSORS")


    print("\nYour Choice")
    player_choose = int(input(": "))

    com_choice = [1, 2, 3]

    print("\nComputer Choice")
    com_choose = (random.choice(com_choice))

    print(": ", com_choose, "\n")


    if player_choose == 1 and com_choose == 1:
        print("\t\tROCK VS ROCK\n")
        print("\t\tDRAW !")
    if player_choose == 1 and com_choose == 2:
        print("\t\tROCK VS PAPER\n")
        print("\t\tYOU LOSE !")
    if player_choose == 1 and com_choose == 3:
        print("\t\tROCK VS SCISSORS\n")
        print("\t\tYOU WIN !")

    if player_choose == 2 and com_choose == 1:
        print("\t\tPAPER VS ROCK\n")
        print("\t\tYOU WIN !")
    if player_choose == 2 and com_choose == 2:
        print("\t\tPAPER VS PAPER\n")
        print("\t\tDRAW !")
    if player_choose == 2 and com_choose == 3:
        print("\t\tPAPER VS SCISSORS\n")
        print("\t\tYOU LOSE !")

    if player_choose == 3 and com_choose == 1:
        print("\t\tSCISSORS VS ROCK\n")
        print("\t\tYOU LOSE")
    if player_choose == 3 and com_choose == 2:
        print("\t\tSCISSORS VS PAPER\n")
        print("\t\tYOU WIN !")
    if player_choose == 3 and com_choose == 3:
        print("\t\tSCISSORS VS SCISSORS\n")
        print("\t\tDRAW !")

    print("PLAY AGAIN ?")
    print ("1. AGAIN, 2. NO")
    player_again = int (input)

    if player_again == 2:
        game()