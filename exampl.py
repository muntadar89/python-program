#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed
def anti_vowel(text):
    vowels = 'AaEeOoIiUu'
    s = ''
    s2 = ''
    for item in text:
        if (item in vowels):
            s2 = s2 + item
        else:
            s = s + item
    return s


