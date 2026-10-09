# Challenge: Write a function to check if a given number is a pronic number.
# a pronic number is a number that is the product of 2 consecutive integers.
# so n is pronic if i and i+1 is such that n = i * ( i + 1 )

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/is-number-pronic/info

def is_pronic(n):
    # every number below till n can be checked to see if it makes n
    for i in range(n):
        # if (i) and (i+1) equals n it is a pronic number
        if (i * (i+1) == n):
            return True
        else :
            continue
    
    # if true has not been returned it is not a pronic number
    return False

if __name__ == "__main__":
    print(is_pronic(6)) # Is a pronic number = True
    print(is_pronic(16)) # Is not a pronic number = False
    print(is_pronic(20)) # Is a pronic number = True
