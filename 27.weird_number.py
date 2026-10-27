# Challenge write a function to check if a number is weird.
# If number is odd it is 'weird'
# if the number is even and in the inclusive range of 2-5 = 'not weird'
# if its even and in the inclusive range of 6 - 20 = 'weird'
# if even and greater than 20 = 'not weird'

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/weird-numbers/info

def is_weird(n):
    # If it is even
    if (n % 2 == 0):
        # in range of 2 and 5
        if (n >= 2 and  n <= 5):
            return 'Not Weird'
        # in range of 6 and 20
        elif ( n >= 6 and n <= 20):
            return 'Weird'
        # every other num
        else:
            return 'Not Weird'
    else:
        # it is odd = 'Weird'
        return 'Weird'

if __name__ == "__main__":
    print(is_weird(3)) #'Weird'
    print(is_weird(25)) # 'Weird'
    print(is_weird(18)) # 'Weird'
    print(is_weird(4)) # ' Not Weird'