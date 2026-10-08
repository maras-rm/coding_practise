# Challenge: Code a spongecase - where a input can change the text where letters alternatly appear in lower and upper case starting with lower case. 

# Challenge can be found: https://app.programiz.pro/community-challenges/preview/spongecase/info

def to_spongecase(text):
    # textALt is what the answer will be
    # i is the counter to determine whether to be caps or lower case
    textAlt = ''
    i = 0

    # for each char in text
    for letter in text:
        # if letter is a space add space to alt text
        if (letter == " "):
            textAlt += letter
        else:
            # if i is even or odd it will be lower or upper case and the counter is updated
            if (i % 2 == 0):
                textAlt += letter.lower()
                i += 1
            else:
                textAlt += letter.upper()
                i += 1

    # print the different case
    print(textAlt)


if __name__ == "__main__":
    to_spongecase("hello world")
    to_spongecase("learn to code")