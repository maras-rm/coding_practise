# Challenge: Write a function to correct a sentence.
# To Correct a sentence, capitalize the first letter and add a full stop at the end if it's not already there.

# challenge can be found here: https://app.programiz.pro/community-challenges/preview/correct-sentence/info

def correct_sentence(sentence):
    # Find the last char of sentence
    endOfSentence = sentence[-1]

    # if there is a full stop - only capitalise first letter
    if (endOfSentence == "."):
        sentence = sentence[0].capitalize() + sentence[1:]
    # else add a full stop and capitalise first letter
    else: 
        sentence = sentence[0].capitalize() + sentence[1:] + "."

    # print result of the sentence
    print(sentence)

if __name__ == "__main__":
    correct_sentence('this is a test')