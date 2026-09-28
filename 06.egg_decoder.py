# Challenge: accept a user input - the code as it appear on a stamped egg. (Just the code, not the Best Before Date)
# Use this code to output the farming method this egg originated from: (Organic, Free range, Barn or Cage)
# Output the country of Origin: e.g.:
# UK: United Kingdom
# NL: Netherlands
# FR: France
# BE: Belgium
# DE: Germany
# ES: Spain
# Output the farm/producer ID

# Extension task 1: 
# A valid code contains at least 7 alphanumerical characters,
# A valid code should start with a number digit between 0 and 3.

# Extension task 2:
# we need to recognise all the possible two-letter country codes. 
# use full list of country codes in the from txt file - 'egg_country_codes.txt'.

# Challenge can be found here: https://www.101computing.net/egg-code-stamp-decoder/ 

def farmingMethod(number):
    # depending on the starting number return farming method
    match number:
        case 1:
            return "Free Range"
        case 2:
            return "Barn"
        case 3:
            return "Cage"
        case _:
            return "Organic"

#pre extension 2 
def countryOriginPreEx2(countryCode):
    # depending on country code return country
    match countryCode:
        case "NL":
            return "Netherlands"
        case "FR":
            return "France"
        case "BE":
            return "Belgium"
        case "DE":
            return "Germany"
        case "ES":
            return "Spain"
        case _:
            return "United Kingdom"

def countryOrigin(countryCode):
    #need a lookup from txt file:
    with open("egg_country_codes.txt", 'r') as file:
        for line in file:
            # skip any empty lines
            if not line.strip():
                continue
            
            # values are split by commas in txt file so key = country
            if ',' in line:
                key, value = line.split(',' , 1)

                key = key.strip()
                value = value.strip()

                # if the key matches the code from the egg return the country
                if (key == countryCode):
                    return value

    # if no country is found return string
    return "No country found"



def eggDecoder():
    eggStamp = input("Enter the egg code: ")

    # To be a valid egg code - must be 7 chars long
    while len(eggStamp) < 7: 
        print("ERROR: a egg code must be a minimum of 7 characters.")
        eggStamp = input("Enter the egg code: ")

    # when 1st char is not a digit
    while (not (eggStamp[0].isdigit())):
        print("ERROR: a egg code must start with a digit, and contain only alphabet or numbers.")
        eggStamp = input("Enter the egg code: ")

    # only accept alphabet and numbers:
    while (not (eggStamp.isalnum())):
        print("ERROR: a egg code must contain only alphabet or numbers.")
        eggStamp = input("Enter the egg code: ")

    # when the 1st char is not between 0 - 3
    while (int(eggStamp[0]) < 0 or int(eggStamp[0]) > 3 ):
        print("ERROR: a egg code must start with a digit between 0 and 3.")
        eggStamp = input("Enter the egg code: ")
        

    # Splitting
    # 1 char = Farming method
    eFM = eggStamp[0]
    # 2/3 char = Country origin
    eCO = eggStamp[1] + eggStamp[2]
    # 4/5/6/7 = Farm ID
    eFId = eggStamp[3:]

    

    fm = farmingMethod(int(eFM))
    co = countryOrigin(eCO.upper())

    print("Egg Farming method: " + fm)
    print("Egg Country Origin: " + co)
    print("Egg Farm id: " + eFId)

if __name__ == "__main__":
    eggDecoder()