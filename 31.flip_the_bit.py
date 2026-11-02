# Challenge: write a function to flip the bits of a given inetger
# Return the number obtained after flipping all bits.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/flipping-bits/info

# e.g input: 5 output: 2
# because 5 = 101 flipping the bits = 010 which is 2

def flip_bits(n):
    # get the binary of the number - is type str:
    bN = bin(n)[2:] 

    # var to keep track of flipped bin
    flip = ''

    # for every value in binary add opposite to flip var
    for digits in bN:
        if digits == '1':
            flip += '0'
        elif digits == '0':
            flip += '1'

    # var to calculate num from bin
    valueOfFlip   = 0     
    
    # for every index in flip
    for i in range(len(flip)):
        # starting with number intialised at 0 (so reverse order using negative indexing)
        # the bit is multiplies by its positional val - power of 2
        valueOfFlip  += int(flip[-(i+1)]) * (2 ** i)


    # return the value of the flipped bin as an int
    return(valueOfFlip)

if __name__ == "__main__":
    print(flip_bits(5))