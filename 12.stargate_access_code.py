# Challenge: Find 3 letter combo to ulock the door.
# Using brute force - iterate through 3 letter combo of the alphabet from AAA to ZZZ and calculate product of their ASCII value.
# If the product matches the given 6 digit number - you have found the valid combination 

#Stargate Access Code - Python Challenge - www.101computing.net/stargate-access-code-python-challenge
import time,os,sys

# Typing print was included from the challenge link above
def typingPrint(text):
    # Slows down typing
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
      

def threeLetterCombo(accessCode):
    # aValues will contain ascii value - for the corresponding alphabet letter
    aValues = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # record ASCII values:
    for letter in alphabet:
        aValues.append(ord(letter))
    
    # for every letter combo (in 3's) find the code (multiplied)
    for firstValue in aValues:
        for secondValue in aValues:
            for thirdValue in aValues:
                count = firstValue * secondValue * thirdValue
                # if code matches the door
                if (count == accessCode):
                    # Figure out ascii numbers INDEX:
                    firstIndex = aValues.index(firstValue)
                    secondIndex = aValues.index(secondValue)
                    thirdIndex = aValues.index(thirdValue)

                    # Match index to letter in alphabet
                    firstLetter = alphabet[firstIndex]
                    secondLetter = alphabet[secondIndex]
                    thirdLetter = alphabet[thirdIndex]

                    # Combine 3 letters for combo and return it
                    combo = firstLetter + secondLetter + thirdLetter
                    return (combo)

                # If does not match go to next combo
                else:
                    continue

if __name__ == "__main__":
    print("    ___________________________________")
    print("   /                                   \\")
    print("   |    Stargate Door Access Panel     |")
    print("   \\___________________________________/")
    print("")

    accessCode = 365820 # This code can be replaced with the code that appears on your access door panel!

    time.sleep(1)
    typingPrint(" >> 6-digit Access Code: " + str(accessCode))
    time.sleep(1)
    typingPrint(" >>")
    time.sleep(1)
    typingPrint(" >> Starting Brute Force Code Breaking Algorithm to retrieve 3-Letter combination...")
    time.sleep(1)
    typingPrint(" >>")
    time.sleep(1)

    # call function - (returns combo) - let user know combo
    combo = threeLetterCombo(accessCode)
    typingPrint(" >> The access code is ...")
    time.sleep(1)
    typingPrint(" >>")
    time.sleep(1)
    typingPrint(" >> " + combo)
    time.sleep(1)