#the program searches for a number in a text or string.

import re
def searchTellNumber(text):
    tellNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    find = tellNumberRegex.search(text)
    print(find.group())


searchTellNumber("hello there we are open for calls at 20:30 this are a available lines 253-256-5656")
