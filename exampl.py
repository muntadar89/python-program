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

#Define a function called count that has two arguments called sequence and item.
#Return the number of times the item occurs in the list.
def count(sequence,item):
  count = 0
  for i in sequence :
    if i == item :
      count = count + 1 
  return count
print (count([1,2,3,1],1))

#Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result
def purify(list_num):
  count = 0
  s =[] 
  for i in list_num :
    if (i%2)==0 :
      s.append(i)
  return s   
print (purify([1,2,3]))

#Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
#or example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
def product(list_int):
  product = 1
  for i in list_int :
    product = product * i 
  return product
print(product([4,5,5]))

#Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
#fr example: remove_duplicates([1, 1, 2, 2]) should return [1, 2]
def remove_duplicates(l):
  s=[]
  for i in l :
    if i not in s :
      s.append(i)
  return s
print (remove_duplicates([4, 5, 5, 4]))
