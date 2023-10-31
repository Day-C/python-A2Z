import random

print("i am thinking of a number from 1 t0 20")

tries = 1
num = random.randint(1, 20)
guess = int(input("make a guess: "))
while guess != num:

    if guess > num:
        print("your guess is heigher")
        guess = int(input("make a guess: "))
        tries = tries + 1
        continue
    elif guess < num:
        print("your guess is lower")
        guess = int(input("make a gues: "))
        tries = tries + 1
        continue
print("Good job you guesses the number in {} guesses!".format(tries))

