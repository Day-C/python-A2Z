#this programm  ask user to enter the correct password

passward = "123456"
while True:
    pss = input("enter our passwoard: ")

    if pss == passward:
        print("welcome sir")
        break
    else:
        print("sorry wrong passward try again latter")
        continue


