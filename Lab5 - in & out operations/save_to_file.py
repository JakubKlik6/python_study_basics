filename = r'c:\\temp\\saving.txt'

line = 'Europe'

cities = ['London', 'Berlin', 'Paris', 'Warsaw', 'Madrid', 'Rome']

file = open(filename,'w+')

file.write(line)
file.write("\n")
#file.writelines(cities)

for city in cities:
    file.write(city+'\n')

file.close()


print('\n---------------')
print('TASK')
print('\n---------------')


import os

webaddresses = []

line = input("Please enter website adress www.")

while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

print(webaddresses)

dirname = os.getcwd()

filename = input("Please eneter filename: ")

filepath = os.path.join(dirname,filename)

file = open(filepath,'w+')

for webaddress in webaddresses:
    file.write(webaddress+"\n")
file.close()

print(os.getcwd())

print('\n---------------')
print('TASK 2')
print('\n---------------')


import os

filename = input("Enter filename path: ")
#C:\Users\DELL\PycharmProjects\pythonProject

while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename = input('Enter filename to read: ')
    webaddresses = []

    with open(filename, 'r') as file:
        for line in file:
            webaddresses.append(line.replace("\n", ''))
    for line in webaddresses:
        if line.endswith('.pl'):
            print(line, 'is a polish web page')
        else:
            print(line, 'is not a polish web page')

