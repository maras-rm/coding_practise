# Challenge: Write a function to check if an anagram of a string is a subsequence of another string.
# Return True if an anagram of the first string is a subsequence of the second string, otherwise return False.

# Every character in the first string must be accounted for, including duplicates.
# You can rearrange those characters into an anagram.
# That anagram must be obtainable from the second string by selecting characters.
# You may skip characters in the second string, and those skipped characters can be anything.

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/anagramic-subsequence/info


def is_anagram_subsequence(str1, str2):
    firstStringChars = []
    flag = False

    # if empty it is true
    if (str1 == ""):
        return True
    
    # Adding chars to test againt 
    for letters in str1:
        firstStringChars.append(letters)
    
    # looping through list created
    # as a update could just loop through str1
    for letter in firstStringChars:
        count = str1.count(letter)

        # if occurs more than once - see if occurs more than once in str2
        if (count > 1):
            sCount = str2.count(letter)
            # If it occurs more than or equal to the amount in str 1 it can proceed - otherwise not viable = False
            if (sCount >= count):
                flag = True
            else: 
                flag = False
                return flag

        # check if letter is present in str2 - if not = False
        if letter in str2:
            flag = True
        else:
            flag = False
            return flag
    
    
    
    return flag

if __name__ == "__main__":
    # Different Test Cases
    print(is_anagram_subsequence('abc', 'cba')) # should be true as letters are rearranged
    print(is_anagram_subsequence('abc', 'cxbxa')) # should be true as the subsequences of abc exist skipping the x
    print(is_anagram_subsequence('abc', 'ab')) # should be false as the letter c is not present
    print(is_anagram_subsequence('abc', 'def')) # should be false as no letter is present
    print(is_anagram_subsequence('aab', 'ab')) # should be false as second a is not present
    print(is_anagram_subsequence('abc', 'acbc')) # should be true
    print(is_anagram_subsequence('', 'abc')) # should be true as an empty string is conventionally subsequence of an empty string
    print(is_anagram_subsequence('', '')) # should be true as both are empty
    print(is_anagram_subsequence('abc', '')) # should be False as a non-empty string cannot be a subsequence of a empty string
