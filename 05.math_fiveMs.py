# In this Python challenge we will manipulate a list of numbers to calculate the Min, Max, Mean, Median and Mode of all these numbers.
# Challenge based from: https://www.101computing.net/min-max-mean-median-and-mod-flowcharts/

import random

numbers=[]

def generateRandomNums():
    #Let's append a random number of random numbers!
    numbersOfItem = random.randint(5,15)
    for i in range(0,numbersOfItem):
        number = random.randint(0,100)
        numbers.append(number)
    
    print("Our random list of numbers:")  
    print(numbers)

# calculate min value
def minCalculator():
    # record first number in the list
    min = numbers[0]

    for i in range(len(numbers)):
        if (numbers[i] < min):
            min = numbers[i]
    
    print("The min number is: "+ str(min))


# calculate max value
def maxCalculator():
    max = numbers[0]
    for i in range(len(numbers)):
        if (numbers[i] > max):
            max = numbers[i]
    
    print("The max number is: "+ str(max))

# calculate mean
def meanCalculator():
    # add all numbers
    sumOfNums = sum(numbers)
    # divide by how many numbers there are:
    mean = sumOfNums / (len(numbers))
    print("The mean is: " + str(mean))
    

# calculate median
def medianCalculator():
    # sort the list:
    numbers.sort()
    # print ordered list
    print("The sorted list of numbers: ")
    print(numbers)
    lenOfNum = len(numbers)
    # if is even - 2 nums in middle add them and divide by 2
    if (lenOfNum % 2 == 0) :
        # indexed of the middle numbers
        middleNum = round((lenOfNum) / 2) 
        next2 = middleNum - 1
        medVal = ((numbers[middleNum]) + (numbers[next2])) / 2
        print("The median value is: " + str(medVal))
    else :
        # else take middle value
        middleValIndex = round((lenOfNum + 1) / 2)
        print("The middle value is: " + str(numbers[middleValIndex-1]))


# calculate mode
def modeCalculator():
    # calculate which value appears the most:
    #sort list:
    numbers.sort()

    uniqVals = []
    modVals = []
    calcMod = []

    for i in numbers:
        if (i not in uniqVals):
            uniqVals.append(i)
        else: 
            modVals.append(i)
    
    if (len(modVals) == 0 ):
        print("No value is repeated so there is no mode.")
    else:
        # how many times does that appear in the list:
        # make sure no repeated vals
        modVal = set(modVals)
        modVal = list(modVal)
        #for each value compare to num and count appearance
        for i in modVal:
            counter = 0
            for val in numbers:
                if (i == val):
                    counter += 1
                else: 
                    pass
            calcMod.append(counter)

        # find max val: 
        maxVal = max(calcMod)

        #Does this max value appear more than once:
        ListOfMaxValIndex = []

        # for every time the max value appears not the index so we know the corresponding value
        for i in range(len(calcMod)):
            if calcMod[i] == maxVal:
                ListOfMaxValIndex.append((i))
            else:
                pass
        
        # Print the modal vals:
        TextStatement = "The mode is: "
        lenofListOfMaxVal = len(ListOfMaxValIndex)
        counter = 1

        for indicies in ListOfMaxValIndex:
            if (counter < lenofListOfMaxVal):
                TextStatement += str(modVal[indicies]) + ", "
                counter +=1
            else:
                TextStatement += str(modVal[indicies]) 
        
        print(TextStatement)
        

# To find these with prebuilt functions:
import statistics

def preBuiltFunctions():
    mean1 = statistics.mean(numbers)
    median1 = statistics.median(numbers)
    mode1 = statistics.mode(numbers)
    print(" ---  This solution uses prebuilt functions  --- ")
    print("The min: " + str(min(numbers)))
    print("The max: " + str(max(numbers)))
    print("The mean: " + str(mean1))
    print("The median: " + str(median1))
    #If there is no mode it returns the first one from the list so no error same with if there is multiple
    print("The mode: " + str(mode1))
    


if __name__ == "__main__":
    generateRandomNums()
    minCalculator()
    maxCalculator()
    meanCalculator()
    medianCalculator()
    modeCalculator()
    preBuiltFunctions()