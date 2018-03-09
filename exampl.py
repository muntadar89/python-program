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


