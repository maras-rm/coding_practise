# Challenge: Write a function to calculate the maximum number of ones, threes and nines that can be obtained from a given number.
# Define a function that takes a int as input
# inside the func, calculate the number of ones, threes and nines go into that int
# Return a dictionary with keys as 'ones', 'threes', 'nines' and their respective counts as values

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/ones-threes-nines/info

def calculate_numbers(n):
    # divide the number by 1,3,9
    one = n // 1
    three = n // 3
    nine = n // 9

    # return as a dictionary
    return {'ones': one, 'threes': three, "nines": nine}

if __name__ == "__main__":
    print(calculate_numbers(10)) # {'ones': 10, 'threes': 3, 'nines': 1}