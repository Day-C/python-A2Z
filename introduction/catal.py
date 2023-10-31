# the program lets the user type in a number and keeps calling the catalize() on that number untill the function returns 1.

def catalize(number):
    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

num = int(input("Enter number: "))
catalize(num)
