# Challenge write a function to find the most common character in a given string other than spaces.
# Challenge found here: https://app.programiz.pro/community-challenges/preview/most-common-character/info

# Challenge 2: Write a function to find the char that repeats first in the string
# Challenge found here: https://app.programiz.pro/community-challenges/preview/first-repeating-character/info

def most_common_character(s):
    # A frequency dictionary to track letters 
    charFrequency = {}

    # for characters in the string
    for c in s:
        # Add letter with a counter
        # if that letter is repeating will increase the already present count
        charFrequency[c] = charFrequency.get(c, 0) + 1

    # For the max value:
    # gets the key with max value not the max in the biggest key - if wanted that just use charFrequency
    maxVal = max(charFrequency, key=charFrequency.get)

    print(maxVal, charFrequency[maxVal])

    print(first_repeating_char(s))


def first_repeating_char(s):
    ListOfChars = []

    # for every character in string
    for c in s:
        # if already added to list is the first duplicate so can return
        if c in ListOfChars:
            return ("First repeating character is: " + c)
        else:
            # else there is no duplicate of that letter so gets added to the list
            ListOfChars.append(c)
    
    # if no return was activated there were no duplicates
    return 'No repeating characters.'
             


if __name__ == "__main__":
    most_common_character("hello world 12312") # l 3, First repeating character is l
    most_common_character("racecar") # r 2, First repeating character is c