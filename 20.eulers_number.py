# Challenge: Write a function to calculate Euler number to a specified precision.
# e = 1/0! + 1/1! + 1/2! + 1/3! + ...
# e.g. input = 5    output = 2.70833

# challenge found here: https://app.programiz.pro/community-challenges/preview/euler-numbers/info

def factorial(n):
    # Stopper for recurring function so cannot keep going forever
    if n < 2:
        return 1
    else:
        # multiplys the number x recalling function with 1 smaller - until reaches basecase above
        return n * factorial(n-1)

def calculate_euler(precision):
    e = 0 

    # for every number upto the input number
    for i in range(precision):
        # eulers calculation function is applied
        e += 1/factorial(i)

    # return rounded value to 5 dp
    return(round(e,5))

if __name__ == "__main__":
    print(calculate_euler(5))