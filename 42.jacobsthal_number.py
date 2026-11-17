# Challenge: Write a function to calculate the jacobsthal number of a given index.

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/jacobsthal-numbers/info

def jacobsthal(n):
    # base case
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    
    # the formula for jacobsthal number using recursion 
    else: 
        return (jacobsthal(n-1) + 2*(jacobsthal(n-2)))

if __name__ == "__main__":
    print(jacobsthal(1)) # 1
    print(jacobsthal(2)) # 1
    print(jacobsthal(3)) # 3
    print(jacobsthal(4)) # 5
    print(jacobsthal(5)) # 11
    print(jacobsthal(6)) # 21