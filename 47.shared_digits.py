# Challenge: Write a function to find and return the digits that are shared between 2 given numbers

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/shared-digits/info

def shared_digits(num1, num2):
    sameNums = []

    # for every digit in the first number
    for n in str(num1):
        # if it is present in the second number add it to the list
        if (n in str(num2)):
            sameNums.append(n)

    # return the shared numbers between the 2 digits
    return sameNums

if __name__ == "__main__":
    print(shared_digits(12345, 64835)) # ['3' , '4' , '5']