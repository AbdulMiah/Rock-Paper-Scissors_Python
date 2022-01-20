import random, os, sys, time

def play():
    os.system("cls")
    rps = ["rock", "paper", "scissors"]
    flag = True
    userPts = 0
    compPts = 0

    player = input("Hello Player! What is your name?\n>> ").capitalize()
    print("\nWelcome "+player)

    while (flag):
        CPU = random.choice(rps)

        print(f"\n{player}'s Score: {userPts}")
        print(f"Computer Score: {compPts}")
        user = input("\nRock, Paper or Scissors?\n>> ").lower()
        if (user == "quit" or user == "exit"):
            for x in range (0,4):
                b = "Quitting Game" + "." * x
                print (b, end="\r")
                time.sleep(0.5)
                flag = False

        elif (user not in rps):
            print("Incorrect Input!\n")
            time.sleep(0.5)
            os.system("cls")
            continue

        print("")

        if (user == CPU):
            print(f"\nYou chose {user} and Computer also chose {CPU}\nIt's a TIE!")

        elif (user =="rock" and CPU =="scissors") or (user=="paper" and CPU=="rock") or (user=="scissors" and CPU=="paper"):
            userPts += 1
            print(f"You chose {user} and Computer chose {CPU}\n+1 Point to {player}!")

        else:
            compPts += 1
            print(f"You chose {user} and Computer chose {CPU}\n+1 Point to Computer!")

        if_win(player, userPts, compPts)

        print("")
        time.sleep(3)
        os.system("cls")


def if_win(player, userPts, compPts):
    if (userPts==3 and compPts==2):
        print("\nThat was intense! Computer was 1 point behind you! Great job {}, you won with {} points!".format(player, userPts))
        time.sleep(1)
        sys.exit()

    elif (userPts==3 and compPts==1):
        print("\nWell Done {}, you won! Play again and try not to give the computer a point!".format(player))
        time.sleep(1)
        sys.exit()

    elif (userPts==3 and compPts==0):
        print("\nYou didn't even give the computer a chance! Congrats {}, you won!".format(player))
        time.sleep(1)
        sys.exit()

    elif (compPts == 3):
        print("\nUnlucky! Computer won this time with {} points!\nPlay again and try to beat the Computer!".format(compPts))
        time.sleep(1)
        sys.exit()


if __name__ == "__main__":
    play()
