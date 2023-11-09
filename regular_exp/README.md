
#
Regular expressions(regex) is a way to match petterns in a string. they allow us to search for specific sequences of characters or partsof strings, that follow a certain rule. 

To implement regex in python we use the 're' module

Regular expressions consist of a pattern and optional flags that specify how the parttern should be interpreted.

HERE are some basic regex concepts:

    '.'     matches any single character except for a newline.
    '\w'    matches any word character (alphanumeric plus underscore)
    '\W'    matches any non-word character
    '\d'    matches any digit
    '\D'    matches any non-digit
    '\s'    matches any whitespace character
    '\S'    matches any non-whitespace character
    '^'     matches the start of a string
    '$'     matches the end of a string
    '|'     matches either the expression before or after it
    '(' and ')'     capture a group of characters.
    '*'     matches zero or more occurrences of the preceding expressoin
    '+'     matches one or more occurrences of the preceding expression
    '?'     matches zero or more occurrences of the preceding expression
    '{}'    specifies a quantifier for the preceding expression
    '[]'    defines a character class.
    '-'     matches a range of characters


the list goes on and on...

