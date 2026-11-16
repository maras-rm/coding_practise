# Challenge: write a function to check if differences between all consecutive paris are 2.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/two-is-difference/info

def two_is_difference(numbers):
    a = 0
    for n in numbers:
        # if is the first number set a
        if (numbers.index(n) == 0):
            a = n
        # if a + 2 is equal to n - difference is 2
        # set a for next number
        elif (a + 2  == n):
            a = n
        # else difference is not 2 hence return false
        else:
            return False
    
    # if it makes it to the end then between consecutive pairs the difference is 2
    return True

if __name__ == "__main__":
    print(two_is_difference([1,3,5])) # True
    print(two_is_difference([1,4,5])) # False
    print(two_is_difference([6,8,10])) # True