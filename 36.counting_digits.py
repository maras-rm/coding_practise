# Challenge: Write a function to count the number of even or odd digits in a list of ints
# Define a func that takes 2 arguments: a list of int (number) and boolean is_evem
# if is_even is True, return a list containing the num of even digits in each of the number in the list.
# else return a list containing the number of odd digits in each number in the list

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/count-evenodd-digits-in-integers/info

def count_digits(numbers, is_even):
    # to keep track of odd and evens per num
    numOfList = []

    # for every number in the list of numbers
    for num in numbers:
        countPerNum = 0 
        # if is_even was set to true
        if (is_even):
            # for the digits in the number
            for digits in str(num):
                # if it is even
                if int(digits) % 2 == 0 :
                    # count update
                    countPerNum += 1

        # else if it is odd
        else:
            # for the digits in the number
            for digits in str(num):
                # if the digit is odd
                if int(digits) % 2 == 1 :
                    # count update
                    countPerNum += 1

        # add the count of odd or even for that number in the list
        numOfList.append(countPerNum)
    
    # return the list of count of the odd/even per num
    return (numOfList)


if __name__ == "__main__":
    print(count_digits([1234, 5678] , True)) # expected out [2,2]
    print(count_digits([1234, 56789] , False)) # expected out [2,3]