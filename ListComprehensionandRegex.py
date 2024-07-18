firstSentence = ['I', 'am', 'playing', 'xbox', 'and', 'trying', 'hard']
secondSentence = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']

print("1. ", [x for x in firstSentence+secondSentence if len(x) >= 3])
print("2. ", [x for x in firstSentence if x[0] == "a"])
print("3. ", [x[-2:] for x in firstSentence])
print("4. ", [x for x in firstSentence+secondSentence if len(x) % 2 == 0])
print("5. ", [firstSentence.index(x) for x in firstSentence if len(x) % 2 == 0])
print("6. ", [x for x in firstSentence+secondSentence if len(x) >= 6])
print("7. ", [x for x in firstSentence if x in secondSentence and len(x) <= 2])
print("8. ", [x for x in firstSentence if x in secondSentence])
print("9. ", [x[0].upper() + x[1:] for x in firstSentence])
print("10. ", [x.replace('a', 'e' * 2)  for x in firstSentence])
print("11, ", [(x,y) for x in firstSentence for y in secondSentence if x != y  and firstSentence.index(x) == secondSentence.index(y)])
print("12. ", [(x,y) for x in firstSentence for y in secondSentence if x == y])
print("13. ", [x+y for x in firstSentence for y in secondSentence if len(x) < len(y) ])
print("14. ", [firstSentence.index(x) for x in firstSentence if x in secondSentence])
print("15. ", [(x[0],y[0]) for x in firstSentence for y in secondSentence])

# ---------------------------------------- Regex ----------------------------------------
import re


text_file = open("lowerwords.txt")
words = text_file.readlines()




def filterList(regex, words):
    return [x for x in words if re.search(regex, x)]



print("1. Words ending with d:", len(filterList(r'd$', words)))
print("2. 4 letter words ending with e:", len(filterList(r'^.{3}e$', words)))
print("3. Vowel as 2nd letter: ", len(filterList(r'^.[aeiou].*', words)))
print("4. End with 2 vowels: ", len(filterList(r'^.*[aeiou]{2}$', words)))
print("5. Start and end with same consonant: ", len(filterList(r'^(\w).*\1$', words)))
print("6. 4 vowels in a row: ", len(filterList(r'.[aeiou]{4}', words)))
print("7. er 3 times: ", len(filterList(r'^[er]{3}', words)))
print("8. 2 letter sequence 3 times: ", len(filterList(r'.*(\w{2}).*\1.*\1.*$', words)))

print("9. 2 letter reversed: ", len(filterList(r'(\w)(\w).*\2\1.*\1\2', words)))
print("10. 3 pairs of double letters in a row: ", len(filterList(r'(\w)\1.*(\w)\2.*(\w)\3', words)))
print("11. Triple pattern that appears twice: ", len(filterList(r'(\w)(\w)\1.*\1\2\1', words)))
print("12. 3 letter palindromes in a row: ", len(filterList(r'(\w).\1(\w).\2(\w).\3', words)))













