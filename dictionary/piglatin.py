
# The latin is a program that alters English words. if the word begins with a vowel, the word 'yoy' is added to the end of it. if the word begins with a consonant or consonant cluter (like ch or gr), the consonant or cluster is momed to the end of the world followed by 'ay'
'''
print('Enter the message  to translated'.center(50, '='))
message = input(': ')

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
pigLatin = []

for word in message.split():
    #separate non letters at the start of the word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters = word[0]
        word = word[1:]
    if len(word) == 0:
        piglatin.append(prefixNonLatters)
        continue
#separate the non-letters at the end of the word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        sufffixNonletters= word[-1] + suffixNonLetters
        word = word[:-1]
#Remember if the word was in uppercase or lowwer case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #change the word to a lower case for translation

#Separate the consonants at the start of the word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants + word[0]
        word = word[1:]
#Add the pig latin ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
#Set the word back to uppercase of title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
#Add add the non-letter back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

#join all the word back together into a single string
print(' '.join(pigLatin))
'''
