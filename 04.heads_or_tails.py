# Challenge: 5 rounds of heads and tailes, each round :
# - the user will make a guess
# - the computer will flip a coin
# - the player will score 1 point for a correct guess

# Extension 1: Tweak the code so that the user can only enter the value “Heads” or “Tails” and nothing else. (If they do, the program should ask them to re-enter their guess until they enter a valid guess.)
# Extension 2: Add some code so that when the 5 rounds are over, the user is given the option to either start a new game or to quit.

# Challenge based off of flowchart found here: https://www.101computing.net/heads-or-tails/    

import random

def flipCoin():
    # A function to randomly choose and return either heads or tails
    number = random.choice([1,2])
    if (number == 1):
        return "Heads"
    else:
        return "Tails"

def hOrT():
    # score tracker
    score = 0

    # Best out of 5
    for i in range(5):
        print("---  Round: "+ str(i+1) + " ---")
        usersGuess = input("Heads or Tails: ")

        # anything other than heads and tails gets rejected
        while usersGuess.capitalize() != "Heads" and usersGuess.capitalize() != "Tails":
            # If not plural correct but accept
            if (usersGuess.capitalize() == "Head"): 
                usersGuess = "Heads"
            elif (usersGuess.capitalize() == "Tail"): 
                usersGuess = "Tails"
            else:
                print ("Error, please enter Heads or Tails")
                usersGuess = input("Heads or Tails: ")
        
        # flip coin and inform user of result
        coinRes = flipCoin()
        print("Coin flipped: "+ coinRes )

        # if correct update score
        if (coinRes == usersGuess.capitalize()):
            print("Good Guess")
            score += 1
        
        else:
            print("Better luck next time!")
        
        # let user know score post round
        print("Your score: " + str(score) + " out of " + str(i+1))

    # Would the user like to restart the game or quit
    restartOrQuit()

def restartOrQuit():
    # If user wants to q or r options
    question = input("Would you like to quit or restart the game? (Q or R) : ")
    # Only let user move on with a q or r option
    while (question.capitalize() != "Q" and question.capitalize() != "R"):
        print ("Error, please enter whether you want to restart game (R) or quit game (Q)")
        question = input("Would you like to quit or restart the game? (Q or R) : ")
    
    # depending on q or r will quit or restart
    if (question.capitalize() == "Q"):
        return
    else:
        hOrT()


if __name__ == "__main__" :
    hOrT()