import random


def play():
    dict = {
        -1: "scissor",
        0: "stone",
        1: "paper",
    }
    userInput = int(input(
        "Enter your Choice( \n 1-> paper, \n0->stone, \n-1->paper\n)"))
    sysInput = random.choice([-1, 0, 1])
    print(dict)
    print(
        f"Your Choice {dict.get(userInput)}, System Choice {dict.get(sysInput)}")

    if (userInput == sysInput):
        print("Its a Draw")

    else:
        if (sysInput == -1):
            if (userInput == 0):
                print("You Won !!")
            else:
                print("You Lost")

        if (sysInput == 1):
            if (userInput == -1):
                print("You Won !!")
            else:
                print("You Lost")

        if (sysInput == 0):
            if (userInput == 1):
                print("You Won !!")
            else:
                print("You Lost")


play()
