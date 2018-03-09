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

#Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word
def scrabble_score(word):
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
  s = word.lower()
  total = 0
  for item in s :
    if item != " " :
      total = total + score[item]
  return total
print (scrabble_score("python"))

"""Write a function called censor that takes two strings, text and word, as input. 
It should return the text with the word you chose replaced with asterisks. 
For example:
censor("this hack is wack hack", "hack")
should return:     "this **** is wack ****" """
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
      if i == word:
        words[count] = stars
      count += 1
    result =' '.join(words)
    return result

print censor("this hack is wack hack", "hack")
