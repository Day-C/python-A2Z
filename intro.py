#1. variables: A variable is a container that stores a value. in python a variable is a name given to the memory location containing something(data).
p = 552
    #p is a the name given to the memory location where 552 is stroed.

x = "hello"
y = True

#2. Data types: data types are a way of classifying data into categories based on it's form, structure, and behaviour.data types determin how data is stored and manipulated. python has several built-in data(integers, floats, strings, booleans, lists, dictonaries, tuples, sets).

    #integers: whole numbers like 1, 2, 3..., as well as negative whole numbers
    a = 22
    b = -546
    
    #floats: decimal numbers like 3.14, 25.4, -1.52 etc
    a = 1.25
    b = 2546.25

    #strings: sequence of characters enclosed on quots(single and double ) like "hello", "friends"
    a = "hello world"
    b = 'power'

    #booleans: logical values and can be either True or False
    a = True
    b = False

    #lists: an  ordered collection if items which can be of different data types and enclosed with square brackets
    a = [1, 2, 3]
    b = [[1, 2], ["red", "blue"]]

    #Tuples: tuples are similar to list but are inmutable(can not be changes). tuples are defined by using parentheses (), and elements are separated by commas
    a = ("python", "is", "cool")
    b = (1, 2, 3, 4)

    #dictionaries(dict): a dictionary is an unordered collection of key-value pairs. where each key is unique and maps to a specific value. they are defined by using curly braces{} and keys are separated from values using colon ( : )
    a = {"name": "jack", "age": 30}
    b = {1:"red",2:"black",3:"blue"}

    #sets(set): the set is an unordered collection of unique elements. it is a mutalbe data structure(can be modified after creation). sets are defined using the curly braces {}, and elements are separated by commas.
    a = {1, 2, 3, 4, 5}
    b = {"pyton"}


#3. Basic Operators: python have various operators for different operations:
    #Arithmetic operators: (+, -, *, /)
    #comparison operators: (==, !=, >, <, >=, <=)
    #Assignment operators: (=, +=, -=, *=, /=, %=(modulus))
    #logical operators: (and, or, not)

#4. conditional statments: conditional statements allow us to write code with more than one outcome: (if, else, elif)

x = 20;
if x > 15:
    print("higher")
elif x == 15:
    print("exactly")
else:
    print("no")

#5. loops: loops allow us to execute a block of code repeatedly for a specific number of times. python had two main loops (for, while).
    #for loop: iterates over a sequence (like a list or tuple) and execute a block of code for each item.
colors = ["green", "red", "blue", "black"]
for color in colors:
    print(color)

    #while loop: a while loop executes a block of code as long as a certain condition retains true.
i = -2
while i < 5:
    print(i)
    i += 1


#6. functions: a funcion is a reusable block of code that can take inputs (parameters) and produce outputs. they help organize code and make it more modular.
def say_hi(name):
    print("hello " name #the say_hi function take a name as parameter.
          #the function prints hello and name

say_hi("john")
    #the above line call the function and passes john as a parameter.


#7. modules: modules are pre-writen code libraries that can be imported into your own script to use their functions and variables

import dandom
random_number = random.randint(1, 6)
print(random_number)
