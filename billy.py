import random
# intro
print("python rock, paper, scissor")
# quit the game or not, initially don' quit
doQuit = False

def quit():
    choice = input("press any key to keep playing, press q to quit \n")
    if choice == "q":
        return True
    else:
        return False

def computer_play():
    r = random.randint(1, 3)
    match r:
        case 1:
            return "r"
        case 2:
            return "p"
        case 3:
            return "s"


def user_play():
    user = input("r, p, s \n")
    while user != "r" and user != "p" and user !=  "s":
        user = input("please input again. r, p, s \n")
    return user

# decides who wins
def compare(u, c):
    # possible ways in which first player can win
    wins = [("r", "s"), ("p", "r"), ("s", "p")]
    if u == c:
        return "draw"
    for i in range(0, 3):
        if wins[i][0] == u and wins[i][1] == c:
            return "user"
        else:
            return "computer"

def count_wins(winner, wins):
    if (winner == "user"):
        return wins + 1
    else:
        return wins

def count_loses(winner, loses):
    if winner == "computer":
        return loses + 1
    else:
        return loses



# the actual program

wins, loses = 0, 0

while not doQuit:

    computer = computer_play()
    user = user_play()

    print("user: " + user)
    print("computer: " + computer)

    winner = compare(user, computer)



    print(winner)

    wins = count_wins(winner, wins)
    loses = count_loses(winner, loses)

    doQuit = quit()
    print("------------------------------------------")

if (wins > loses):
    print("you won!")
elif (wins < loses):
    print("you lost!")
else:
    print("its a draw!")
print("GAME OVER")








