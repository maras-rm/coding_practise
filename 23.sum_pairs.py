# Challenge: Write a function to find all pairs from 2 lists whose sum is equal to a given number
# return a list of tuples where each tuple represents a pair of numbers whose sum is equal to a given number.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/list-pairs-with-sum-x/info

# eg. input: [1,2,3] [2,3,4] 5  output: [(1,4), (2,3), (3,2)]

def find_pairs(lst1, lst2, x):
    # The list that will contain the tuples that make the sum
    finalSum = []

    # for every number in list 1
    for numbers in lst1:
        # for every number in list 2
        for secondN in lst2:
            # if the numbers sum is equal to x
            if ((numbers + secondN) == x) :
                # create numbers into a tuple
                t = tuple((str(numbers), str(secondN)))

                # add tuple to the list
                finalSum.append(t)
    
    # returns the list of tuples that equal x
    return finalSum

if __name__ == "__main__":
    print(find_pairs([1,2,3], [2,3,4], 5))