import re

def LongestWord(sen):
    # remove all punctuation from the string
    sen = re.sub(r'[^\w\s]','',sen)
    # split the string into words
    words = sen.split()
    # find the longest word
    longest_word = max(words, key=len)
    return longest_word


# function call
print(LongestWord(input()))
