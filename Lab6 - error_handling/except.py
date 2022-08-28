import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many persons are there in the team?')
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except ValueError as e:
    print('Sorry - you need to enter an integer number',e)

except ZeroDivisionError as e:
    print('Sorry - you nedd to enter value > 0',e)

except:
    print('Something went wrong...', sys.exc_info()[0])

print('Every person should have around', tasksPerPerson, 'tasks')


print('\n ---------------')
print('TASK')
print('\n ---------------')

import sys

file_path = r'c:\temp\orders.txt'

with open(file_path, "r") as file:
    for line in file:

        line = line.replace('\n', '')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                  (pharmacy_name, item, amount))

        except ValueError as e:
            print("There is a problem with incorrect data conversion in line: ",line,e)

        except IndexError as e:
            print('Missing information in line: ',line,e)

        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])

print("Processing finished")
