'''
number = 1
previousNumber = 0

while number < 50:
    print("Sum: ",number + previousNumber)
    previousNumber = number
    number += 1
'''


import random
my_number = random.randint(0,20)        #generate random number
trials = 0
guess = -1

print("Guess my number")

while guess != my_number:
    guess = int(input())
    trials += 1
    if guess == my_number:
        print("You are right! It was:",my_number,"You needed",trials,"trials.")
    elif guess > my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")



