# write a function to find the sum of odd numbers in a list.
# if even numbers are given skip
# challenge found: https://app.programiz.pro/community-challenges/preview/add-odd/info

def sum_of_odds(numbers):
    soN = 0
    # for every number in the list of numbers
    for num in numbers:
        # if even go to next number
        if (num % 2 == 0):
            pass
        else:
            # if odd add 
            soN += num
    
    # return the sum of all odd numbers
    return soN

if __name__ == "__main__":
    print(sum_of_odds([1,2,3,4,5]))