# Challenge Quiz 1: Where in the world
# Randomly select a building - display its name and height 
# ask user to guess the country this building is from. - Out of 10 - at the end ask if want to play again.

# Quiz 2 - Which building is taller 
# display the name and location of 2 buildsings and ask the player which is taller
# the quiz should keep going until incorrect answer is given

# Give user the option of what game they would like to play

# Extension: Give a third option where user can ask for a fact about the building - which consists of where it is and it's height.

# For building info use the file: "iconic-buildings.csv"
# World Buildings Quiz - www.101computing.net/world-buildings-quiz

import random

file = open("iconic-buildings.csv","r")
buildings = file.readlines()
file.close()


def generateBuilding():
    building = random.choice(buildings).split(",")
    name = building[0]
    height = int(building[1])
    city = building[2]
    country = building[3]
    return name, height, city, country

def whereInTheWorld():
    score = 0
    print("***  You have chosen: where in the world is this building?  ***")

    for i in range(10):
        name, height, city, country = generateBuilding()

        # Show name and height
        print("The name of this building is: ", name, " and it's height is: ", height)

        # ask for country
        usersGuess = input("Where do you think this building is from (country)? ")

        # check
        if (usersGuess.casefold() == country.casefold()):
            print("That is correct! The building ", name, " is found in ", country)
            score += 1
        else:
            print("That is incorrect. The building ", name, " is found in ", country)
    
    print("Your score is: ", str(score), " out of 10.")

def whichBuildingIsTaller():
    score = 0
    questionsAsked = 0
    correct = True
    print("***  You have chosen: which building is taller?  ***")

    while (correct):
        # generate buildings to compare
        name, height, city, country = generateBuilding()
        secondName, secondHeight, secondCity, secondCountry = generateBuilding()

        # If you get 2 same buildings need to change
        while (secondName == name): 
            secondName, secondHeight, secondCity, secondCountry = generateBuilding()

        # tell name and location of the building
        print("From these two options: ")
        print("1. "+ name +" which is located in ", city + ", " + country + ".")
        print("2. "+ secondName +" which is located in ", secondCity + "," + secondCountry + ".")
        # ask which is taller:
        usersGuess = int(input("Which building do you think is taller (1,2)? "))

        while (usersGuess != 1 and usersGuess != 2):
            print("Please enter 1 or 2 for which building you think is taller ")
            usersGuess = int(input("Which building do you think is taller (1,2)? "))

        if (usersGuess == 1):
            # if first building is taller
            if (height > secondHeight):
                print("Correct the " + name + " is taller than the " + secondName)
                print(name + " height is: " + str(height))
                print(secondName + " height is: " + str(secondHeight))
                score += 1
            
            else:
                print("Incorrect the " + name + " is smaller than the " + secondName)
                print(name + " height is: " + str(height))
                print(secondName + " height is: " + str(secondHeight))
                correct = False
        
        else : 
            if (height < secondHeight):
                print("Correct the " + secondName + " is taller than the " + name)
                print(secondName + " height is: " + str(secondHeight))
                print(name + " height is: " + str(height))
                score += 1
            
            else:
                print("Incorrect the " + name + " is taller than the " + secondName)
                print(name + " height is: " + str(height))
                print(secondName + " height is: " + str(secondHeight))
                correct = False
    
    print("You got: " + str(score) +" correct.")


def didYouKnow():
    print("***  You have chosen a fact  ***")
    name, height, city, country = generateBuilding()
    print("Did you know?")
    print(name + " is located in " + city + ", " + country + ".")
    print("It is " + str(height) + " meters tall.")


def menuItems():
    print("    /\                           /\           ")
    print("   |  |   / \     / \     __    |  |    /\    ")
    print("   |  |   | |  _  | |    /  \    ||    /  \   ")
    print("   |  |   | |_/ \_| |   |    |   ||   /    \  ")
    print("___|  |___| |     | |____\  /____||__/      \ ")
    print("")
    
    print("Welcome! This is the buildings quiz! ")
    print("Game 1 is where in the world is this building?")
    print("***   Game 1 explanation   ***")
    print("You will be given a building name and it's height.")
    print("You have to guess the country you think this building is from.")
    print("You will be asked 10 questions, and get a score at the end.")
    print("")
    print("Game 2 is which building is taller?")
    print("***   Game 2 explanation   ***")
    print("You will be given 2 building names and where they are located.")
    print("You have to guess which building is taller.")
    print("You will be asked questions until you get one wrong.")
    print("")
    print("If you do not want to play a game you can learn a fact.")
    print("Option 3 is a fact about buildings")
    print("***   what a fact may include   ***")
    print(" A fact will tell you about a building, ")
    print(" where that building is located, ")
    print(" the height of that building. ")
    print("")

    print("The options are: ")
    print("1. Game 1 - where in the world is this building?")
    print("2. Game 2 - which building is taller?")
    print("3. A building fact")
    usersChoice = int(input(" Please choose from the options: "))
    print("")

    while(usersChoice != 1 and usersChoice !=2 and usersChoice != 3):
        usersChoice = int(input(" Please choose from the options: "))

    match (usersChoice):
        case 2:
            whichBuildingIsTaller()
        case 3:
            didYouKnow()
        case _:
            whereInTheWorld()


if __name__ == "__main__":
    #whereInTheWorld()
    # whichBuildingIsTaller()
    menuItems()

