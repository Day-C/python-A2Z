
#the keys(), values(), and items() methods
# this are the three dictionaty methods that will return list-like values of a dictionary's keys, values, or both


balls = {'color': 'green', 'sport': 'tenis'}
    
#using a for loop to iterate over each value in balls dictionary and prints values
for v in balls.values():
         print(v)           #output: green \n  tenis



#get() method: Dictionaries have a get() method that takes two arguments: the key of the value to be retrived and a fallback value to return if the key does not exist

ID = {"name": "braiden", "age": 45}
print("{}'s ID number is {}".format(id[name], str(ID.get('number', 0))))
        #output: braiden's ID number is 0


#sefdefault() method: the setdefault is used when we have to set a default value for a certain key, only if the key does not already have a value
light = {"range": "1km", "consumption": "24kw\h"}
for 'color' not in light:
    light['color'] = "white"

#OR

light.setdefault('color', 'white')
 

#
for k in balls.keys():
         print(k)           #output: color \n sport


for i in balls.items():
    print(i)                #output: ('color', 'green') \n ('sport', 'tenis')


for v, j in balls.items():
         print("key: {}, Value: {}".format(v, j))


#character countiong program.

message = "It was a bright cold day in April, and the birds flew to the west"

coount = {}
for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

print(count)
