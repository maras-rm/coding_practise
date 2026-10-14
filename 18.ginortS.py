# Challenge: Write a function to stort a string in ginortS order.
# all sorted lowercase to upper case letter to digits sorted by odd then even
# eg. 'Sorting1234' should return 'ginortS1324'

# Challenge can be found: https://app.programiz.pro/community-challenges/preview/ginorts/info 

def ginortS(s):
    # variables to sort string into
    caps = ""
    lowChars = ""
    oddNums = ""
    evenNums = ""

    # for characters in string
    for char in s:
        # if it is uppercase - add to caps var
        if (char.isupper()):
            caps += char
        # else if it is lowercase - add to lowChars var
        elif (char.islower()):
            lowChars += char
        # else if it is numerical 
        elif (char.isnumeric()):
            # if number is even add to evenNums else oddNums var
            if (int(char) % 2 == 0):
                evenNums += str(char)
            else:
                oddNums += str(char)
    
    # sorted() takes the string and sorts the chars by ASCII / unicode values and returns it as a list
    # ''.join() takes the list of sorted chars and glues it back to a string with no spaces between sorted letters
    caps = ''.join(sorted(caps))
    lowChars = ''.join(sorted(lowChars))
    oddNums = ''.join(sorted(oddNums))
    evenNums = ''.join(sorted(evenNums))

    # the overall string orders by: lowCase - upperCase - oddNums - evenNums
    overallString =  lowChars + caps + oddNums + evenNums
   
    # print the overall string
    print(overallString)

if __name__ == "__main__":
    ginortS("Sorting1234")
