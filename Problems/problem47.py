# The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file high-score.txt’ which is either blank or contains the
# previous high-Score. You need to write to it whenever the game() function breaks the
# high-score.

import random

def game():

    print("Game Loading....")

    # creating a score
    score = random.randint(1,100)
    print(f"Your score is {score}")

    #loading highscore
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore == ""):
            highscore = 0
        else:
            highscore = int(highscore)

    # updating highscore
    if(score>highscore or highscore == 0):
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
