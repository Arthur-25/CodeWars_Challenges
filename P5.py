'''
Write a function that takes in a string of one or more words, and returns the same string,
but with all words that have five or more letters reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
'''

def invert_string(str):
    inverted_str = ""
    for number in range(len(str)-1,-1,-1):
        inverted_str += str[number]
    return inverted_str

def spin_words(str):
    str += " "
    new_str = ""
    word = ""
    for number in range(0,len(str),1):
        if (str[number] != " "):
            word += str[number]
        else:
            if(len(word)>= 5):
                new_str += invert_string(word)
            else:
                new_str += word
            new_str += " "
            word = ""

    return new_str.rstrip()


print(spin_words("Welcome"))
print(spin_words("to"))
print(spin_words("CodeWars"))

print(spin_words("Hey fellow warriors"))
print(spin_words("This sentence is a sentence"))