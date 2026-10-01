# Challenge: Ask user the year of their dob
# Inform the user of their chinese zodiac sign which matches their birth year

# Extension 1: With the year matching your date of Birth you can also work out what is your Chinese Zodiac element.
# To do so you wil need to check the the last digit of your birth year. if this last digit is:
# 0 or 1: Your element is Metal
# 2 or 3: Your element is Water
# 4 or 5: Your element is Wood
# 6 or 7: Your element is Fire
# 8 or 9: Your element is Earth

# Extension 2: each zodiac has specific attributes which can be used to describe the year to come - use a dictionary and display the corresponding description of the zodia sign

# Chinese New Year Coding Challenge found here - www.101computing.net/chinese-new-year-coding-challenge/


# The following array is pre extension 2
zodiacSigns = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit", "Dragon","Snake","Horse","Ram"]
    
# The following dictionary is for extension 2
zodiacSignsDictionary = {
    "Monkey":"Intelligent, playful, and clever, the Monkey is resourceful and loves solving problems with wit and charm.",
    "Rooster":"Confident, honest, and hardworking, the Rooster is practical, ambitious, and detail-oriented.",
    "Dog":"Loyal, trustworthy, and protective, the Dog is compassionate and always stands up for what’s right.",
    "Pig":"Generous, kind-hearted, and sincere, the Pig is known for its honesty, hard work, and love of comfort.",
    "Rat":"Intelligent, resourceful, and quick-witted, the Rat excels in finding opportunities and achieving success.",
    "Ox":"Strong, determined, and reliable, the Ox is known for its hardworking nature and steadfast loyalty.",
    "Tiger":"Bold, adventurous, and confident, the Tiger is a natural leader who thrives on challenges.",
    "Rabbit":"Gentle, compassionate, and creative, the Rabbit seeks peace and harmony in its surroundings.",
    "Dragon":"Charismatic, powerful, and ambitious, the Dragon is a symbol of strength and good fortune.",
    "Snake":"Wise, intuitive, and elegant, the Snake is calm and strategic, with a deep understanding of the world.",
    "Horse":"Energetic, free-spirited, and optimistic, the Horse loves adventure and pursues goals with enthusiasm.",
    "Ram":"Creative, gentle, and empathetic, the Goat seeks beauty and tranquillity, often expressing artistic talents." 
}

def findZodiacYear(year):
    # divide the birth year by 12 and get the modulo
    yearDivd = year % 12

    # look at the modulo - and that is the zodiac sign
    zodSign = str(zodiacSigns[yearDivd])
    zodSign1 = str(list(zodiacSignsDictionary)[yearDivd])
    
    #print("The year: " , str(year) , " has the zodiac sign of: " , zodSign)    # - this is pre extension 2
    print("The year: " , str(year) , " has the zodiac sign of: " , zodSign1)
    
    # Get the value from dictionary - based on zodiac
    desc = zodiacSignsDictionary.get(zodSign1)
    print("The year has the following qualities: ", desc )

def findZodiacElement(year):
    # Find the last number of the year
    lastNum = int(str(year)[-1])
    
    # Based on the number of the year you get the element
    if (lastNum == 0 or lastNum == 1):
        print("Your Chinese zodiac element is Metal.")
    elif (lastNum == 2 or lastNum == 3):
        print("Your Chinese zodiac element is Water.")
    elif (lastNum == 4 or lastNum == 5):
        print("Your Chinese zodiac element is Wood.")
    elif (lastNum == 6 or lastNum == 7):
        print("Your Chinese zodiac element is Fire.")
    else:
        print("Your Chinese zodiac element is Earth.")
    return




if __name__ == "__main__":
    year = int(input("Enter a year (e.g. the year you were born): "))

    findZodiacYear(year)
    findZodiacElement(year)