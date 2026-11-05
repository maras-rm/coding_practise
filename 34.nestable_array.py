# challenge: write a function to check if one list can be nested in another.
# - Check if minimum of 1st list is greater than minimum of 2nd list
# - and if the maximum of 1st list is less than the maximum of 2nd list
# e.g. [1 , 2 , 3 , 4] [0 , 6] result = True
# Reason: The min/max of first list = 1,4 
# The min/max of second list = 0,6
# since both condition are met (min 1st list > min of 2nd list and max of 1st list < max of 2d list) one list can be nested in another.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/nestable-array/info

def can_be_nested(list1, list2):
    # Min / Max val of list 1
    minValList1 = min(list1)
    maxValList1 = max(list1)

    # Min / Max val of list 2
    minValList2 = min(list2)
    maxValList2 = max(list2)

    # If min val from l1 is bigger than min val of l2 AND 
    # If max val from l1 is less than max val of l2 
    # Return relevant flag
    if (minValList1 > minValList2) and (maxValList1 < maxValList2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(can_be_nested([1,2,3,4] , [0,6]))