'''
age = 23

if age >= 18:
    print('You are adult and u can buy alcohol')
else:
    print('You are to young')

isDrunk = True

if age >= 20 and not isDrunk:
    print('You are adult and u can buy alcohol')
else:
    print('You are to young')

isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print('You are adult and u can buy alcohol')
else:
    print('You are to young')
'''

MinLikes = 500
MinShare = 1000
numLikes = 600
numShare = 900

if numLikes > MinLikes and numShare > MinShare:
    print("discount 10%")
else:
    print("Not enough likes or shares")

######################################################

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('you received free burger')
else:
    print('there is no discounts today')

#######################################################

diskSize = 140
diskSizeUsed = 133
fileSize = 10

if diskSize - diskSizeUsed >= fileSize:
    print('The file can be downloaded')
else:
    print('There isn\'t enough free disk space to download the file. Sorry :(')
