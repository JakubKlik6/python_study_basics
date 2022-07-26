data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for person in data:
    print(person)

print("-------------")

for person in data:
    elements = person.split(":")
    print(elements[0].upper())
    print(elements[1])

print("-------------")

for person in data:
    elements = person.split(":")
if elements[0] == "Error":
    print(elements[1].upper())
else:
    print(elements[1])

//////////////////////////////////////////

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for number in range(9):
    print(string_A)

print("xxxxxxxxxxxxx")

for number in range(9):
    if number %2 == 0:
        print(string_A)
    else:
        print(string_B)

print("xxxxxxxxxxxxx")

for number in range(10):
    print(number * "x")

print("xxxxxxxxxxxxx")

for number in range(10):
    if number%2 == 0:
        print(number*"x")
    else:
        print(number*"o")

        
////////////////////////////////////////////////

i = 10
result = 1
score = 1

for x in range(1,i+1):
    result *= x

print("10!= ",result)


print("------------------")

for x in range(1,11):
    score *= x
    print(x,"! =",score)

print("------------------")

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(noun,adj)
