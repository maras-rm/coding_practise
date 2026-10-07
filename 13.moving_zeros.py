# Challenge: Return a integer with all the zeros moved to the end:
# eg. 1020304050 = 1234500000

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/zeros-to-end/info

def move_zeros_to_the_end(n):
    # Counter for amount of 0
    howManyZeros = 0
    overallNum = ''

    # for each number value from input
    for num in (str(n)):
        # if = 0 update counter
        if (num == "0"):
            howManyZeros += 1
        # else add the number value to the overallNum that will be returned
        else:
            overallNum += num
    
    # for amount in the counter add those 0 to the end of the overall num
    for i in range(howManyZeros):
        overallNum += "0"
    
    # return the overall num which has the zeros at the end
    return(overallNum)
    



if __name__ == "__main__":
    print(move_zeros_to_the_end(1020304050))
    print(move_zeros_to_the_end(1000203045))
    print(move_zeros_to_the_end(5230007091))