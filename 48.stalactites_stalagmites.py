# Challenge: Write a function to determine whether a given string represents stalactites or stalagmites.
# Top half of string = stalactites
# Bottom half of string = Stalagmites
# Return stalatites if there are more non space chars (#) in upper half of string and stalagmites if there are more chars in lower half.
# if they are equal return both

# Challenge can be found: https://app.programiz.pro/community-challenges/preview/stalactites-or-stalagmites/info

def identify_formation(s):
    # Split spring into halves
    firstHalfOfString = s[:(len(s)//2)]
    secondHalfOfString = s[(len(s)//2):]

    # counter vars
    fcCount = 0
    scCount = 0

    # for every character in the first half of string
    for chars in firstHalfOfString:
        # if space skip
        if chars == " ":
            continue
        # if char update count
        else:
            fcCount +=1

    # for every character in the second half of string
    for chars in secondHalfOfString:
        # if space skip
        if chars == " ":
            continue
        # if char update count
        else:
            scCount +=1

    # if first half has more chars than spaces than the second half
    if (fcCount > scCount):
        return ("Stalactites")
    # else if second half has more chars than spaces than the first half
    elif (fcCount < scCount):
        return ("Stalagmites")
    # else they have the same amount of chars than spaces
    else:
        return("Both")


if __name__ == "__main__" :
    print(identify_formation('#####\n    #\n    #\n    #')) # "Stalactites"
    print(identify_formation('#####\n    #\n    #\n ####')) # "Both"
    print(identify_formation('#\n    #\n    #\n ####')) # "Stalagmites"