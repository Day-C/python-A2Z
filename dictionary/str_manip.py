#this section we will be looking at some of the varois way to manipulate strings with python

#escape character(\): the excate characteris used what otherwise is imposible to put in a string


# cl = "the teacher said "we are to stay in class for an hour""
cl = "the teacher said \"we are to stay in class for an hour\""

#Raw string: by puting an 'r' in the begining of a string to make it a row string is another way;

print(r'this is carol\'s car.')

#multiple strings with triple quotes:

print('''Dear Alice,

      hope you are doing fine now i was writing to  inform you

      those with you are more than those agains you!
sincerely,
Joshua''')
    #triple quotes are also used to make a multi-line comment
       """ this is a comment """

#strings can be regarded as lists because they are a collection of character. so they can also be manipulated by indexing.
s = "hello clear"
s[0]            #output: 'h'

s[0:5]          #output: 'hello '

f = s[6:]       #output:  'clear'


#in and not operators: these two operators an be used with strings just like list values
se = 'hello' in 'hello, world'          #output: True

se = "world" not in "hello world"       #outpur: False

#f-strings: have the f prefix before the starting wuotation mark
name = "Rishel"
age = 45
print(f"hello MRS {name}. next year will be {age + 1}")     #hello MRS Rishel. next year you will be 46

#upper(), lower(), isupper(), isupper() methods: the upper() and lower() methods return a new string with all the letters in the original string have been converted to upper of lowercase, respectively.Nunletter character in the string remains unchanged
name = "Ethien"
name = name.upper()         #output: 'ETHIEN'
greet = "HELLO WORLD"
greet = greet.lower()       #output:  'hello world'

print(isupper("NOW"))       #output:  'True'
print(islower("NOW"))       #output:  'false'
print(isalpha("top"))       #output:  'True' cheks if string is made up of only alphabetical letters
print(isalnum("5645ksi"))    #output:  'True' if string is made up of alphabetic letters and numbers
print(isdecimal("12564554"))  #output: True check if string is made up of decimal numbers

#justikfy text with rlust(), ljust(), and center() moethods
# the rjust() and ljust() return a padded version of the string they are called on with space inserted to justify them

"hello".rjust(5)            #output:'     hello'
"hello".rjust(5, '*')       #output:'*****hello'
"hello".ljust(5, '#')       #output:'hello#####'
"hello".center(6, '*')      #output:'***hello***'

#removing characters with strip(), rstrip(), and lstrip() methods:
word = "     hello"
print(word.strip())         #output:'hello'
word = "stiptrostprikponostirks"
print(world(strip('stri')))  #output: 'ptrokponoks'


#number values of characters with ord(), and chr() functions:
#because computers only understand binary, every character have and special number dedicated to it (ASCII numbers)
print(ord('A')          #output: 64
print(chr(64)           #output: 'A'
