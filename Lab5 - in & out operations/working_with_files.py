'''
file = open("c:\\temp\\joke.txt","r")       #open files

content = file.read()
print(content)

file.close()

print("\n--------------\n")

with open("c:\\temp\\joke.txt",'r') as file:
    content = file.read()
    print(content)

print("\n--------------\n")

with open("c:\\temp\\joke.txt",'r') as file:        #working with big data
    for line in file:
        print(line)
file.close()

print("\n--------------\n")

fragment = file.read(10)
while fragment:
    print(fragment)
    fragment = file.read(10)

file.close()
'''

print("\n--------------\n")
print("TASKS")
print("\n--------------\n")


file_path = r'c:\temp\data_input\orders.csv'

with open(file_path,"r") as file:
    
    for line in file_path:
        line = line.replace('\n',' ')
        order = line.split(',')

        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)

print("Processing finished")
