# Challenge: Write a function to find the longest consecutive ascending sequence in a list of numbers.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/consecutive-ascending-numbers/info

def longest_consecutive_sequence(numbers):
    # prevNum - var to track previous number
    # tracker - list to add consecutive number lists to
    # list count - what list to add to in track as is list of lists
    prevNum = 0
    tracker = []
    ListCount = 0
    
    # for elements in the numbers
    for n in numbers:
        # set first number - and add to the trackers list a list with first num
        if (len(tracker) == 0):
            prevNum = n
            tracker.append([n])

        # if is a conscutive num
        elif (prevNum + 1 == n):
            # add to the list and update previous number
            tracker[ListCount].append(n)
            
            prevNum = n

        else:
            # start new list in the tracker with next number
            # update the listCount - so adds to the new list you just started
            # update prev num
            tracker.append([n])
            ListCount += 1
            prevNum = n
            
    # var to see which list is longer within the lists (tracker) and what index it is on
    longerList = 0
    longerListIndex = 0

    # for len of lists in tracker 
    for i in range(len(tracker)):
        # if that list is bigger than the previous one it showed that is updated along with its index
        if len(tracker[i]) > longerList:
            longerList = len(tracker[i])
            longerListIndex = i

    # the list with the longest consecutive amount is returned
    return(tracker[longerListIndex])

if __name__ == "__main__":
    print(longest_consecutive_sequence([1,2,3,1,2,3,4])) # [1,2,3,4]
    print(longest_consecutive_sequence([11,12,13,14,15,3,4])) # [11,12,13,14,15]