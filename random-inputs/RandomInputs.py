import time

from GamesInfo import *
import random

# Game Select
gamePrompt = "Enter one of the following games: "
for key, value in gameList.items():
    gamePrompt += "| {} |".format(key)

givenInputs = ""
selectedGame = ""
inputPause = ""

# Outputting keys
def ButtonPress(inpList):
    while True:
        rndInput = random.choice(inpList)
        output(rndInput)
        time.sleep(inputPause)

selectedGame = input(gamePrompt).upper()
for key, value in gameList.items():
    if selectedGame == key:
        givenInputs = value
    else:
        pass

if givenInputs != "":
    inputPause = float(input("How much time should go by between random inputs? (RECOMMENDED in-between 0 and 1): "))
    isReady = input("Write 'GO' to start. Write 'CANCEL' to stop the program. ").upper()
    if isReady == "GO":
        for i in range(10, 0, -1):
            print("Starting in {} seconds".format(i))
            time.sleep(1)

        print("Gaming has begun")
        ButtonPress(givenInputs)

    else:
        print("Operation cancelled ")

else:
    print("Give a valid game")
