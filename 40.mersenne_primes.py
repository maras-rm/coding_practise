# Challenge: write a function to find all mersenne primes up to a given number.
# a mersenne num = M_p = 2^p - 1 where p is a int
# 1, 3, 7, 15, 31, 63, 127 , 255, 511
# but primes are = 3, 7, 31, 127

# challenge can be found: https://app.programiz.pro/community-challenges/preview/mersenne-primes/info

def isprime(n):
    flag = False
    # not a prime
    if n == 0 or n == 1:
        return False
    # if greater than 1
    elif n > 1:
        # from 2 onwards till number
        for i in range(2, n):
            # if it is divisible not a prime number
            if (n % i) == 0:
                flag = True
                break
        
        # IF flag = true it is not a prime number
        if flag:
            return False
        else:
            # prime number has been found
            return True

def mersenne_primes(n):
    mersenne_n = []

    for i in range(n):
        # mersenne calculation
        num = (2**(i+1)) - 1

        # if that number is bigger than n we can stop the looping
        if (num > n):
            break

        # if that mersenne number is a prime number it gets added to the list
        if (isprime(num)):
            mersenne_n.append(num)

    # Prints the prime mersenne numbers in range 
    print(mersenne_n)

if __name__ == "__main__":
    mersenne_primes(130)