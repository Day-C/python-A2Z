arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = arr[0:-2]

def show(lists[]):
    for i in lists:
        print(i)


show(arr)                       #output: [1, 2, 3, 4, 5, 6, 7, 8]


#changing item of an array
arr[0] = 0                     #output: [0, 2, 3, 4, 5, 6, 7, 8]


#delete item from an array
del(arr[0])               
show(arr)                       #output: [2, 3, 4, 5, 6, 7, 8]


#list concat and replication
r = ['A', 'B', 'C']

s = arr + r
show(s)                         #output: [2, 3, 4, 5, 6, 7, 8, 'A', 'B', 'C']

s = r * 2
show(s)                         #output: ['A', 'B', 'C', 'A', 'B', 'C']


#check if item is in a list
print('A' in r)                 #output: True
print('B'not in r)              #outpur: False


#enumerate(): on each instance of the loop, the enumerate() return 2 , we have {}".format(index, item))
#output: At index[0] we have seconds\n At index[1] we have minutes\n...

#random(): to chose a random item from the list we can use random.randchoice()
import random
print(random.randchoice(a))
            #random.shuffle() rearanges the list 


#**** methods
#append():values
a = ["seconds", "minutes", "hours"]
for index, item in enumerate(a):
    print("At index[{}], we have {}".format(index, item))
    #output: At index[0] we have seconds\n At index[1] we have minutes\n...


#random(): to chose a random item from the list we can use random.randchoice()
import random
print(random.randchoice(a))
            #random.shuffle() rearanges the list 


#**** methods
#append(): this method is used to add an item into a list
b = [1, 2, 3]
b.append(4)
show(b)             #output: [1, 2, 3, 4]



#insert(): this method insert an element at a specified index
b.insert(3, 4)
show(b)             #output: [1, 2, 3, 4]



#remove(): the remove method is passed the value to be removed form a list
b.remove(4)
show(b)             #output: [1, 2, 3]



#sort():rearages items of a list
c = ["rat", "dog", "cat", "ant"]
c.sort()        #----c.sort(reverse=True) if this was the case list will be reverse

show(c)             #output: ["ant", "cat", "dog", "rat"]
                    #we cwn only sort items of the same type



