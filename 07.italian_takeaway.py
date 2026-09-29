# Challenge: a italian takeaway is asking
#  - facilitate ordering - by code
#  - calculate total of order
# They have stored menu in text file: 'food_menu.txt' - data is : Code;Description;Price;

# Extension : add input validation so only valid codes can be entered
# - must start with a letter: C,D,S,P,W,X
# - After depending on the letter the number can be up to a certain range
# Challenge found here: https://www.101computing.net/italian-takeaway-ordering-system/

# Extra - let the user know a mini summary - so what they have ordered and the individual price of that item, before the final cost

def checkNumber(letter, num):
    # Depending on the letter the number can only be a certain value - if it can be a number it returns true
    match(letter):
        case "P":
            if (num < 0 or num > 10):
                return False
        case "X":
            if (num < 0 or num > 2):
                return False
        case "C":
            if (num < 0 or num > 2):
                return False
        case "D":
            if (num < 0 or num > 4):
                return False
        case "W":
            if (num < 0 or num > 2):
                return False
        case _: # s = 4
            if (num < 0 or num > 4):
                return False
    
    return True
            

def containLetter(foodOrder):
    # If first letter is a valid letters - calls to check number - if everything is good returns true 
    # as long as one code is valid - that should get ordered
    isValidCode = False
    for food in foodOrder:
        firstLetter = food[0].upper()
        numValue = food[1:]
        if firstLetter in "CDSPWX":
            isValidCode = True
            isValidCode = checkNumber(firstLetter, int(numValue))
        else:
            # If wanted to fail if they had at least one non valid code would change isValidCode here to false and return
            continue
    
    return isValidCode

def foodOrdering():
    # User input for food order
    foodCodes = input("Please enter the codes of food you will like to order: ")

    # User input split by ,
    foodOrder = foodCodes.split(',')
    notValidCode = containLetter(foodOrder)
    
    # If is not a valid code (from validation) repeats question
    while not (notValidCode):
        print("There was a error with one of your codes")
        foodCodes = input("Please enter the codes of food you will like to order: ")
        foodOrder = foodCodes.split(',')
        notValidCode = containLetter(foodOrder)

    totalPrice = 0.0

    print("You have ordered: ")
    
    # opens menu
    with open("food_menu.txt", "r") as file:

        for lines in file:

            # if there are empty lines ignore
            if not lines.strip():
                continue

            # splits by semicolons
            if ";" in lines:
                Code, Description,Price, punctuation = lines.split(";" , 3)

                # clean up data so no spaces etc
                Code = Code.strip()
                Description = Description.strip()
                Price = Price.strip()
                Price = float(Price)


            
            for oc in foodOrder:
                # for every ordered food it checks against the known code and adds the price if matches ( this way you can order multiple of same code)
                if (oc.upper() == str(Code)):
                    # For what the user has ordered tell the user the price/description - before adding to total
                    print(Description, " which costs: ", str(Price))
                    totalPrice += Price
                
               

        # Lets user know the price
        print("Your total order has come to: £" + str(totalPrice))


if __name__ == "__main__":
    foodOrdering()

