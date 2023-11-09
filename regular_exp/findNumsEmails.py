
import pyperclip, re, sys


#find number regex
numberRegex = re.compile(r'''(
                         (\d{3}|\(\d{3}\))?      #country code
                         (\s|-|\.)              #separator
                         \d{3}            #first set of 3 or 4 numbers
                         (\s|-|\.)              #separator
                         \d{5}            #second set of 3 or 5 numbers
                         (\s|-|\.)              #separator
                                      #optional last three numbers
                         (\s*(ext|X|ext.)\s*\d{2, 5})?  #extension
                         )''', re.VERBOSE)

#find email regex
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9-%+-]           #name
                        @                           #@ symbol
                        [a-zA-Z0-9.]                #domain
                        (\.[a-zA-Z]{2, 5})
                        )''', re.VERBOSE)



#chek 
text = str(pyperclip.paste())

match = []
for group in numberRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phoneNum += ' X' + group[8]
    match.append(phoneNum)

for grroup in emailRegex.findall(text):
    match. append(group[0])


if len(match) < 1:
    print("No phone numbers or e-mails")
else:
    pyperclip.copy('\n'.join(match))
    print('\n'.join(matches))
