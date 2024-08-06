import string

def count_word(text, word):
    counter = 0
    for i in text:
        if i == word:
            counter+=1
    return counter