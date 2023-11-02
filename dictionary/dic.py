

birthday = {'Alen': 'Apr 1', 'Bob': 'Dec 12', 'carol': 'Mar 4'}

while True:
    print("enter a name : (BLANK TO Quit)")
    name = input("\n enter your name: ")

    if name == "":
        break

    if name in birthday:
        print("{}'s birthday is on {}".format(name, birthday[name]))

    else:
        print("i don't have the birthday information of {}".format(name))
        bdy = input("what is your birthday? : ")
        
        birthday[name] = bdy
        print("birthday has been updated")

