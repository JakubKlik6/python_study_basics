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
