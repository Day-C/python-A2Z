# this is a mini calculator program to perform simple operations


def add(first, sec):
    try:
      return (first  + sec)
    except:
        print("sorry something went wrong. Try again!!!")
    

def sub(first, sec):
    try:
        return (first -  sec)
    except:
        print("sorry something went wrong: Try again!!!")

def mul(first, sec):
    try:
        return (first * sec)
    except:
        print("sorry something went wrong: Try again!!!")

def div(first, sec):
    try:
        return (first / sec)
    except:
        print("sorry something went wrong: Try again!!!")

print(add(45, 56))
print(sub(58, 126))
print(mul(235, 565))
print(div(144, 102))
