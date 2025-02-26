'''
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(str):
    abc_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    false_array = [False] * 26
    str = str.lower()
    for number in range(0,len(str),1):
        for num in range(0,len(abc_array),1):
            if (str[number] == abc_array[num]):
                false_array[num] = True
    for number in range(0,len(false_array),1):
        if (false_array[number] == False):
            return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("Cwm fjord bank glyphs vext quiz"))
print(is_pangram("Pack my box with five dozen liquor jugs."))
print(is_pangram("How quickly daft jumping zebras vex."))
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))

print(is_pangram("This isn't a pangram!"))
print(is_pangram("abcdefghijklm opqrstuvwxyz"))
print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))