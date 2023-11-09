
import re

#Here, we pass the desired pattern to re.compile() and store the regex in phoneNumRegex then we call search() on the phoneNumRegex, and pass search() the string we want to match for during search.

phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d')
num = phoneNumRegex.search('this is our company number: 652546256')
print(num.group())          #output: 652546256
    
#grouping (): in the above example say we want to separate the numbers in 3 sections, we cold simply use parentheses to create the groups in regex (\d\d\d)(\d\d\d)(\d\d)

number = re.compile(r'(\d\d\d)(\d\d\d)(\d\d\d)')
find = number.search("this is a number: 256456566")
print(find.group(1))        #output: 256
print(find.group(2))        #output: 456
print(find.group(3))        #output: 566
print(find.group())         #output: 256456566

#pipe(|): we can use the pipe to mache one of several patterns
# In a case where we want ot find the words "'banket', 'benker', 'banking'", we can simply specify a prefix only once.
    #NOTE if all words are in the string, the first occurrance will be returned as the match
heist = re.compile(r'bank(er|ing|et)') #If we had just 2 choices (r'banker|banket")
see = heist.search("the banker goes to work on sunday")
print(see.group())          #output: banker

#OPTIONAL matching with ?:  the ? is ised hen we want ot match an optional character or word
heroRegex = re.compile(r'supper(wo)?man')   #the (wo) group is the optional sting
hero = heroRegex.search("supperman is to the rescure")
print(hero.group())     #output: supperman

hero = heroRegex.search('that is supperwoman')
print(hero.group())     #output: supperwoman

#Match ONE or MORE (*): using the above example we test this method

heroRegex = re.compile(r'supper(wo)*man')
hero = heroRegex.search('supperman to the rescure')
print(hero.group())     #output: supperman

hero = heroRegex.search('there is supperwoman')
print(hero.group())     #ouput: supperwoman

#Matching specific repetition {}:
laughRegex = re.compile(r'(ha){3}')
laughing = laughRegex.search('hahaha that is fun')

print(laughing.group())     #output: hahaha

laughing = laughRegex.search("hahaha")
print(laughing.group())     #output: None

#FINDALL(): The final method will return the stringss of every match in the search string

bdyRegex = re.compile(r'\d\d\/\d\d\/\d\d\d\d')
bdy = bdyRegex.findall("johs birthday is 02/09/1654 and mary's is 12/05/1925")
for i in bdy:
    print(i)        #output: 02/09/1654 \n 12/05/1925

#Creating character clases: some time using the shothand character classes are too general. We can make out own classes to meet out standards

vawelsRegex= re.compile(r'[aeiouAEIOU]')
find = vawelsRegex.findall("It is time to awake!")
print(find)         #output: ['I', 'i', 'e', 'o', 'a', 'a', 'e']


        #Using the Caret character(^): with the caret character you make a negative character class. A negative character class will match all the  characters that are not in the character class.

consonantsRegex = re.compile(r'[^aeiouAEIOU]')
consonant = consonantsRegex.findall("how and why i dint know")
print(consonant)        #output: ['h', 'w', ' ' , 'n', 'd', ' ', 'w', 'h', 'y', ' ' ,'d', 'n', 't', 'k', 'n', 'w']

#Caret and Doller sign: The caret character can be used at the start of a regex to indicate that a match must occure at the beginning og the searched text.On the other hand the dollar sign can be put at the end of the regex ti indicate the string ends with  the regex pattern.
beginRegex  = re.compile(r'^interestingly')
check = beginRegex.search("interestingly this is what they told me")
print(check == None)        #output: false


endingRegex = re.compile(r'\d\d$')
check = endingRegex.search('she was born when he was 23')
print(check == None)        #output: false

#WILDCARD character(.): The Dot or '.' character in regular expressions will match any character excetp for the newline.
        #NOTE the '.' character will match just one character which is why the match of the text "flat" in the example below matches to 'lot'
rimeRegex = re.compile(r'.at')
mention = rimeRegex.findall('at the time they sat down the ant fell flat')
print(mention)


#Matching with DOT-STAR(*): the star character is used when we want to match anything and everything.
    #NOTE: The start character will alwasy try to match as much text as posible. to limit this use the dot star and question mark (.*?)
nameRegex = re.compile(r'first Name: (.*) last Name: (.*)')
names = nameRegex.search('first Name: benjamen last Name: flanklin obi')
print(names.group(1))       #output: benjamen
print(names.group(2))       #output: franklin obi


    #matches to "esclamation followed by anything followed by an esclamation
nameRegex = re.compile(r'!.*?!')
name = nameRegex.search('!to be kind is to be! present')
print(name.group())     #output: !to be kind is to  be!


#matching newline with DOT character: when using '.*', the highers we can match is limited to the newline character. Now here is a way to do this By passing 're.DOTALL' as a second argument to re.compil()

newlineRegex = re.compile(r'.*', re.DOTALL)
all_txt = newlineRegex.search('it is not all you can become.\nyou can be more')
print(all_txt.group())      #is is not all you can become.\nyou can be more


#CASE-INSENSITIVE matching: Normally regex matches exacly the text spcified in that exact case(capital or small letters)
    # to make regex case-insensitive we can pass re.IGNORECASE of re.I as the second argument to re.compile.

nameRegex = re.compile(r'diego', re.I)
names = nameRegex.search("fransisco, is the manage but his boss is Diego")
if name == None:
    print('not here')
else:
    print("he is here")     #output: he is here


#SUBSTITUTING Strings (sub()): The sub() method in Regex takes 2 arguments. The first is the string to replace if a match is found and secong is the string for the regular expression.

nameRegex = re.compile(r'john')
name = nameRegex.sub(r'Diego', 'john is the one you should be looking for')
print(name)


hideRegex = re.compile(r'mr (\w)\w*')
names = hideRegex.sub(r'\1***', 'mr flid, and mr philibers had no choice but go Zee')
print(names)

#READING COMPLEX REGEXES(re.VERBOSE): When writing a complex and long regex it becomes hard for us and others to understand. 're.VERBOSE' tells re.compile to ignore whitespace and comments inside the regular expression string. the "VERBOSE" mode is passed as a second argument to re.compile().

phoneRegex = re.compile(r'''((\d{3}|\(\\d{3}\))?    #county code
                        (\s|-|\.)?                  #separator
                        \d{3}                      #first 3 numbers
                        (\s|-|\.)                   #separator
                        \d{3}                       #second set of 3 numbers
                        (\s|-|\.)                   #separator
                        \d{3}                       #last set of 3 numbers
                        )
                        ''', re.VERBOSE)
number = phoneRegex.findall('call now 237.256.256.561 235-658-849-949 and 874 838 993')
print(number)


#COMBINING Multiple modes: when trying to combine re.VERBOSE to write comments in a regex and at the same time we also want to use re.DOTALL, it becomes unacceptable because re.compile() takes just one value as a second variable. But to overcome this  me make use of the bitwise or operator '|' used to pipe the modes together

allRegex = re.compile(r'hello', re.VERBOSE | re.DOTALL)
find = allRegex.search('there was a voice saying\nhello world\n from within')
print(find)
