#in this section we will look at all the various types of data types, and wht they can do and not do.

#integers(int): integers are whole numbers, like 1, 2 3... they can be positive,negative or Zero;
    #They can be  represented by a single value shuch as 46.
    #integers have no decimals.
    #integers are inmutabel meaning it can not be changed once assigned buy it can only be modified.
    x = 254
    x = x + 2
    print(x)  # output: 256

#floating point numbers(float): floating point numbers are real numbers like 3.14, 253.25. they have a fractional part and can be positive , negative, or zero
    #can be represented by a value with a decimal place, like 3.14.
    #have a mantissa (a fractional part) and an exponent (a power of 10).
    #Are also known as "doubles" because they can be represented a wide range of values
    y = 25.23
    y = y + 1.23
    print(y)   # output: 

#strings(str): strings are sequences of characters, like "hello world". they can contain letters, digits, and special characters.
    #can be define using single and double quotes.
    #can contain any kind of character, including whitespace.
    #strings are inmutable meaning can not be changed once assigned.
    a = "hello wolrd"
    b = 'python is cool'
    print(a + ' ' + b)

#boolean values(bool): booleans are either True of False.  they are used to represent logical conditions.
    #can be represented by literals True or False
    #are inmutable meaning they can not be changed once assigned.
    #Can be used in conditional statements, such as if-else clauses.

    z = True

#Lists(list): lists are ordered collections of items, like [1, 2, 3, 4] or ["black", "green", "blue"]. lists can contain elements if different  types of data types.
    #Lists are defined using square brackets [], and comma separated elements.
    #can contain any number of elements including none.
    #elements can be accessed by index (position) within the list.
    fruits = ["apple", "orange", "banana"]  #creates a list
    n = [10, 20, 30, "more"]    #creates a list
    print(n[0])        #output: 10 first element of the n list.

#Tuples (tuple): tuples are similar to lists, but they are immutable, meaning they cna not be modified ance created.
    # Are defined using parentheses () and commas separating the elements.
    #can contain any number of elements, including none
    #elements can be accessed by index(position) within the tuple.

    fruits = ("apple", "orrange", "banana"      #creates a tuple
    #are mutable, meaning they can be modified after creation
    fruits = ("apple", "orange", "banana")
    numbers = (1, 2, 3, 4)

#sets(set): sets are unordered collections of unique items. unlike lists, sets can not store duplicate items. sets are defined by curly braces {}
              #All elements of a set are unique. sets ingnore duplicates
              #Sets are orderless meaning its element have no specific order.
              #because they are unordered, elements can not be indexed
              #Immutable: sets are immutable meaning they can not be modified after it is created
              s = {1, 2, 3, 4}
              print(s)   #output: 1, 2, 3, 4

#distionaties (dict): Dictionaties are key-value pairs. we can create a dictionary using curly braces {}, and a key must be unuqie. we can retrive, update, and delet items.
              #key-Value pair: in dictionaries each key is unique and maps to a specific value
              dic = {"name":"Edd", "age":17, "profession":"SE"}:q

