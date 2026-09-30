# Challenge: From the file: 'Monarchs-of-England.csv' which lists monarchs in chronological order. Data looks like: StartYear,EndYear,Name.
# get user to enter a year between 725 - 2017
# look up monarch and return answer

# Extension : Tweak the output so that when giving the name of the monarch matching the year entered, you mention the previous monarch and the next monarch
# Challenge was found here: https://www.101computing.net/kings-queens-of-england/ 

def kAndQ():
    # Intro
    print("*****************************")
    print("*       Kings & Queens      *")
    print("*         of England        *")
    print("*****************************")
    print("")

    # GET the year the user wants to know
    year=int(input("Enter a year between 757 and 2026: "))

    # The file only contains data between - so reask if not in range
    while (year < 757 or year > 2026):
        print("Error: please enter a year between 757 and 2026")
        year=int(input("Enter a year between 757 and 2026: "))

    # The file to look up from
    file = open("Monarchs-of-England.csv","r")

    # flags to know prev monarch and if a monarch has been found
    prevMonarch = ""
    haveFoundMonarch = False

    for line in file:
        # skip empty lines
        if not line.strip():
            continue
        
        #split on the comma by : StartYear, EndYear, Name
        if ',' in line:
            startYear, endYear, monarch = line.split(',', 2)

            # clean up data (no space and dates are ints)
            startYear = int(startYear.strip())
            endYear = int(endYear.strip())
            monarch = monarch.strip()

            # Pre-data - if is the first monarch
            if(len(prevMonarch) == 0 ):
                prevMonarch = "Unknown"

            # If monarch has been found - this is the next monarch thats reigning
            if (haveFoundMonarch == True):
                # reset flag - so if reigns overlap we still know next monarch
                haveFoundMonarch = False
                print("The next monarch is: " + str(monarch))


            # if the year is in a rulers dates print the monarch
            if (year >= startYear and year <= endYear):
                print("The monarch that ruled in the year " + str(year) + ": " + str(monarch))
                print("The monarch before was: " + prevMonarch)
                # set flags / update previous monarch
                prevMonarch = str(monarch)
                haveFoundMonarch = True
                continue
            else: 
                # update previous monarch
                prevMonarch = str(monarch)

    
    file.close()

if __name__ == "__main__":
    kAndQ()