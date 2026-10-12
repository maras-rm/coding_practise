# Challenge: write a function to check if a given string can be typed using a broken keyboard
# The broken keyboard can only type certain characters.
# The function should take 2 strings as input. The first string is for working keys, and second string is the word to be typed
# check if each char in the word is present in working keys, returning true if the word can be typed else false.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/broken-keyboard/info

def can_type(keys, word):
    notPresent = False
    # for every letter in word
    for letters in word:
        # if that letter is in the good keyboard characters not present = true
        if letters in keys:
            notPresent = True
        else:
            # if at least one character is not in keys then return false as can't be typed
            notPresent = False
            return notPresent
    
    # return flag
    return notPresent


if __name__ == "__main__":
    print(can_type('abc', 'bad')) # answer = False
    print(can_type('abcdefg', 'bag')) # answer = True