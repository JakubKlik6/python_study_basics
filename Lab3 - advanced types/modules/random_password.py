#ASCII table
#for i in range(32,127):
#    print(i,chr(i))

#random password generator
import random

ints = range(33,127)
password = ''

for i in range(12):
    password += chr(random.choice(ints))

print("Password is: ", password)

print("xx-----------------xx")

import random
min = 1
max = 6
dice = random.randint(min,max)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')

print('----------------------')

dices = []

for i in range(5):
    dices.append(random.randint(min,max))

dices.sort()
print(dices)
