import random
myNymbers = []

while len(myNymbers) < 7:

    newNumber = random.randint(1,49)

    if newNumber in myNymbers:
        print("Eliminated: ",newNumber)
        continue

    myNymbers.append(newNumber)

print("Those number will win:" ,myNymbers)
