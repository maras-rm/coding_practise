# Challenge: Let user open 1/3 doors to see if monster is behind the selected door.
# - count the amount of doors the user openned, and stop once the user meets the monster

# The challenge can be found here: https://www.101computing.net/find-the-monster/

import random

def showDoors():
    # The three doors to choose from
    print(""" 
    _____1_____    _____2____   _____3_____
    |  __  __  |  |  __  __  |  |  __  __  |
    | |  ||  | |  | |  ||  | |  | |  ||  | |
    | |  ||  | |  | |  ||  | |  | |  ||  | |
    | |__||__| |  | |__||__| |  | |__||__| |
    |  __  __()|  |  __  __()|  |  __  __()|
    | |  ||  | |  | |  ||  | |  | |  ||  | |
    | |  ||  | |  | |  ||  | |  | |  ||  | |
    | |  ||  | |  | |  ||  | |  | |  ||  | |
    | |  ||  | |  | |  ||  | |  | |  ||  | |
    | |__||__| |  | |__||__| |  | |__||__| |
    |__________|  |__________|  |__________|""")

def monster():
    # The monster hiding behind the door
	print("""
        .-''-'-''-.
       | .--.-.--. |
       |` >       `|
       | <         |
       (__..---..__)
      (`|\o_/ \_o/|`)
       \(    >    )/
     [>=|   vvv   |=<]
        \__\   /__/
            '-'
 """)

def startGame():
    # Counter so user knows how many doors have been opened in the game
    doorsOpened = 0

    # Intro
    print("Halloween Game")
    print("Avoid the monster!")
    print("Between rounds the monster can move.")
    print("Three doors ahead...")

    # doors to choose from visually
    showDoors()

    # the door the monster is behind
    monsterDoor = random.randint(1,3)

    # ask the user which door they want to look behind
    print("Is the monster behind door...")
    userdoor = int(input("1,2, or 3? "))

    # Validation - so can only enter doors 1/2/3
    while(userdoor != 1 and userdoor != 2 and userdoor != 3):
        print("Error: There are not that many doors. Which door would you like to look behind? ")
        userdoor = int(input("1,2, or 3? "))

    # while the door the user has chosen, does not match the door monster is hiding behind the game continues
    while (userdoor != monsterDoor):
        doorsOpened += 1
        print("Phew! No Monster!")
        showDoors()
        print("You enter the next room ...")
        monsterDoor = random.randint(1, 3)
        userdoor = int(input("1,2, or 3? "))
    
    # if the user chooses door where monster is hidden behind the game ends and the user is told how many doors they opened
    if (userdoor == monsterDoor):
        doorsOpened += 1
        print("  ARGHHHH!  MONSTER")
        monster()
        print("You openned: " + str(doorsOpened)+ " doors before you found the monster.")

    


if __name__ == "__main__":
    startGame()