# Challenge: Write a function to return a list that contains elements with the same parity (odd or even) as the first element of the list

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/same-parity-1/info

def same_parity(numbers):
    # list to keep track of numbers
    listOfNum = []

    # if the first num is even
    if (numbers[0] % 2 == 0):
        # for every number in the list
        for num in numbers:
            # if it is the first number, add it to the overall list
            if len(listOfNum) == 0:
                listOfNum.append(num)
            # else check if the number is even and if so add to the overall list
            elif (num % 2) == 0 :
                listOfNum.append(num)

    # else the first num is odd
    else:
        # for every num in the list
        for num in numbers:
            # if it is the first number, add it to the overall list
            if len(listOfNum) == 0:
                listOfNum.append(num)
            # else check if the number is odd and if so add to the overall list
            elif (num % 2) == 1 :
                listOfNum.append(num)

    # return the overall list which shares a parity with the first num
    return listOfNum


if __name__ == "__main__":
    print(same_parity([1,2,3,4])) # returns [1,3]
    print(same_parity([10,2,3,4])) # returns [10,2,4]