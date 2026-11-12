# Challenge: Write a function to check if  given number is a kaprekar number of not
# Return true if it is a kaprekar num else false.
# a kaprekar num is a number whose square can be split into 2 parts that add upp to the origianl number again.
# you should split the num by how many digits are in the og num
# eg. 45 is True because 45^2 = 2025 and 20 + 25 = 45

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/kaprekar-numbers/info

def is_kaprekar(n):
    # var of squared num
    # len of n - so can know how to split
    squaredNumber = n ** 2
    lenOfN = len(str(n))

    # split the number from the front to back
    firstHalf = str(squaredNumber)[:lenOfN]
    secondHalf = str(squaredNumber)[lenOfN:]

    # sum of split num
    s = int(firstHalf) + int(secondHalf)

    # if matches og num = kaprekar num
    if (s == n ):
        return True
    
    # else split the other way so if 3 digits but 5 nums ending has 3 and beginning has 2 digits etc
    else:
        secondHalf = str(squaredNumber)[-lenOfN:]
        firstHalf = str(squaredNumber)[:-lenOfN]

        # sum of split num
        s = int(firstHalf) + int(secondHalf) 

        # if matches og num = kaprekar num
        if (s == n ):
            return True
        # else not a kaprekar num
        else: 
            return False

if __name__ == "__main__":
    print(is_kaprekar(45) )# TRUE
    print(is_kaprekar(297)) # TRUE
    print(is_kaprekar(9) )# TRUE
    print(is_kaprekar(703)) # TRUE
    print(is_kaprekar(25)) # False