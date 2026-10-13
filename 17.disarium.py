# Challenge: a number is a disarium when the sum of its digits each raised to the power of their position equals the number itself
# eg. 175  - 1^1 + 7^2 + 5^3 = 175 = disarium

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/disarium-number/info

def is_disrium_number(num):
    # var to keep track of sum post powering
    sum = 0

    # for every number in num
    for n in str(num):
        # add to the sum -> n ** the position it is in number + 1 (as counts from 0)
        sum += (int(n) ** (str(num).index(n) + 1))

    # If sum matches the num then it is a disarium and returns true else false
    if (sum == num):
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_disrium_number(175))
    print(is_disrium_number(135))
    print(is_disrium_number(1))