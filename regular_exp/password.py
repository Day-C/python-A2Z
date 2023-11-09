import re

wordRegex = re.compile(r'''(
                        [A-Za-z0-d.-]{8}
                        )''', re.VERBOSE)
capsRegex = re.compile(r'[A-Z]')
numRegex = re.compile(r'[0-9]{2}')
smallRegex = re.compile(r'[a-z]{4}')

password = str(input('enter your passwood: '))
pas = wordRegex.search(password)
num = numRegex.search(password)
caps = capsRegex.search(password)
smalls = smallRegex.search(password)
if pas != None and num != None:
    if caps != None:
        print('strong password')
else:
    print('weak password')

