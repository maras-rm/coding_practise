# challenge: write a function to check if a given number is pandigital
# a pandigital num contains all num from 0 to 9 at least once

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/is-number-pandigital/info

def is_number_pandigital(num):
    allNum = "1234567890"

    # To be pandigital needs all numbers
    for numbers in allNum:
        flag = False
        # for the digits in the number you want to check
        for dig in str(num):
            # if number is found then can move to next digit
            if (numbers == dig):
                flag = True
                break
            else:
                continue
        
        # if a number is not found the flag would remain false making it not pandigital
        if flag == False:
            return ("False: " + str(numbers) + " not found in " + str(num))
    
    
    # if all numbers are found True is returned
    return("True")


if __name__ == "__main__":
    print(is_number_pandigital(1234567890)) # return True
    print(is_number_pandigital(123456790)) # return False: 8 not found in 123456790