# The Challenge is to create a cat age convertor so you can find out how old a cat is in human years. 
# The challenge can be found here: https://www.101computing.net/cat-age-calculator/
# To convert the age of a cat in human years you have to do the following:
# - Year 1 Counts for 15 human years
# - Year 2 Counts for 9 human years
# - Thereafter each year counts for 4 human years.

# Extension 1 : make it work for months pre 1 
# Extension 2 : depending on the age the cat is in a different category as seen below:
#  - kitten = from bith to 6 months
#  - Junior = from 7 months to 2 years
#  - Prime = from 3 years to 6 years
#  - Mature = from 7 years to 10 years
#  - Senior = from 11 years to 14 years
#  - Geriatic = from 15 years above
# Extend your code to tell the end-user what stage of life their cat’s age is corresponding to.


def isCatUnder1Q():
    # Asks is the cat under 1 - only allows y or n answer
    isCatUnder1 = str(input("Is your cat under 1 in years? (Y/N) : ")) 
    while (isCatUnder1.upper() != 'Y' and isCatUnder1.upper() != 'N'):
        print('Invalid input. Please enter Y or N')
        isCatUnder1 = str(input("Is your cat under 1 in years? (Y/N) : "))
    
    return isCatUnder1

def askCatAgeQ(isCatUnder1):
    # Asks for cat age
    if (isCatUnder1.upper() == "Y"):
        ageOfCat = int(input("How old is you cat (in months)? "))
    else: 
        ageOfCat = int(input("How old is you cat (in years)? "))
    return ageOfCat

def howOldIsMyCat() :
    #response to if should expect a month answer or year answer
    isCatUnder1 = isCatUnder1Q()

    convertedAge = 0

    #While answer is yes expect a month answer
    while (isCatUnder1.upper() == "Y"):
        ageOfCat = askCatAgeQ("Y")
        if (ageOfCat < 12):
            monthAge = calculateCatAgeMonths(ageOfCat)
            print("In human years your cat is the equivalent of " + monthAge + " old.")
            catAgeCategory(isCatUnder1, ageOfCat)
            return

        # if answer is above 12 get a reinput - is cat older than 1 if so what age
        else:
            print("Invalid input. You said your cat is not older than 1")
            isCatUnder1 = isCatUnder1Q()

    # while answer is no expect answer in years
    if (isCatUnder1.upper() == "N"):
        ageOfCat = askCatAgeQ("N")

    # the first 2 years have a varied addittion number
    if ageOfCat == 1:
        convertedAge = 15
    elif ageOfCat == 2:
        convertedAge = 15 + 9
    # but then it goes up in steady increments of 4
    else : 
        convertedAge = 15 + 9 
        for i in range (ageOfCat - 2):
            convertedAge += 4
    
    print("In human years your cat is the equivalent of " + str(convertedAge) + " years old.")
    catAgeCategory(isCatUnder1, ageOfCat)

def calculateCatAgeMonths(months):
    # depending on the month it returns the age statement
    if (months >=  12):
        return 
    if (months == 1):
        return "4 to 5 months"
    elif (months == 2):
        return "9 to 10 months"
    elif (months == 3):
        return "2 to 3 years"
    elif (months == 4):
        return "5 to 6 years"
    elif (months == 5):
        return "8 to 9 years"
    elif (months == 6):
        return "10 years"
    elif (months == 7):
        return "11 to 12 years"
    elif (months == 8):
        return "13 years"
    else :
        return "14 years"

def catAgeCategory(isCatUnder1, age):
    #if the cat is measured in months
    if (isCatUnder1.upper() == 'Y'):
        if (age <= 6):
            print("Your cat is in the Kitten cat stage.")
            return
        elif (age >= 7 and age <=12):
            print("Your cat is in the Junior cat stage.")
            return
    # if cat is measure in years
    if (age <=2):
        print("Your cat is in the Junior cat stage.")
    elif (age >= 3 and age <= 6 ):
        print("Your cat is in the Prime cat stage.")
    elif (age >= 7 and age <= 10 ):
        print("Your cat is in the Mature cat stage.")
    elif (age >= 11 and age <= 14 ):
        print("Your cat is in the Senior cat stage.")
    elif (age >= 15):
        print("Your cat is in the Geriactic cat stage.")


if __name__ == "__main__":
    howOldIsMyCat()