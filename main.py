"""
Rock Paper Scissors | THE GAME

Created by: Jo
https://github.com/XxJOxX25
"""



# Imports
import os
import time
import random


# Neccesary functions

def close():
    os.system("cls")
    print("")
    close = input("Press ENTER to close")


def onStart():

    print("Rock Paper Scissors | THE GAME")
    print("")
    print("")
    print("Created by: Jo")
    print("https://github.com/XxJOxX25")
    print("")
    print("")
    print("")

    userStart = input("Do you want to start game Y/N:")

    if userStart == "Y" or "y":
        game()
    else:
        os.system("cls")
        close()

def game():

    os.system("cls")
    print("Rock: 1")
    print("Paper: 2")
    print("Scissors: 3")
    
    print("")

    userInput = input("Your Choice: ")

    os.system("cls")
    generatedNumber = random.randint(1, 3)
    userNumber = int(userInput)

    """
    ROCK: 1
    PAPER: 2
    SCISSORS: 3
    """

    if generatedNumber == 1 and userNumber == 1:
        print("Bot had Rock| Nobody won.")

    elif generatedNumber == 1 and userNumber == 2:
        print("BOT had Rock | Congratulations, you won!")

    elif generatedNumber == 1 and userNumber == 3:
        print("BOT had Rock | You Lost.")

    elif generatedNumber == 2 and userNumber == 1:
        print("BOT had Paper | You Lost.")

    elif generatedNumber == 2 and userNumber == 2:
        print("BOT had Paper | Nobody won.")

    elif generatedNumber == 2 and userNumber == 3:
        print("BOT had Paper | Congratulations, you won!")

    elif generatedNumber == 3 and userNumber == 1:
        print("BOT had Scissors | Congratulations, you won!")

    else:
        print("Unexpected error occured | 0x200")

    
    print("")
    userStart = input("Do you want to start a new game Y/N:")

    if userStart == "Y" or "y":
        time.sleep(1.5)
        game()
    else:
        close()

    os.system("cls")

# Game

onStart() # Main Menu

