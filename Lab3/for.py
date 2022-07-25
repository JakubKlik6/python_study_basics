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
