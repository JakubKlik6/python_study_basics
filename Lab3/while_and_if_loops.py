#if inside while
values = [10,20,11,45,64,48,65,21,98,47,53,65,88]
i = 0
max = len(values) - 2     #lenght of value
print('\tFind three increasing numbers (next to each other)')
print('')
while i<max:
        print(values[i],values[i+1],values[i+2])

        if values[i] < values[i+1] and values[i+1] < values[i+2]:
            print('\tFound: ',values[i],values[i+1],values[i+2])
        i += 1


##############
print('------------------')
print('')
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) - 2          #lenght of value
print('\tFind first number**2 == second number')
print('')

while i<max:
    print(numbers[i], numbers[i + 1])
    if numbers[i+1] == numbers[i]**2:
        print('\tFound: ',numbers[i],numbers[i+1])
    i += 1

##############
print('------------------')
print('')

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) - 3          #lenght of value
print('\tFind firs number**2 = second number and second number**2 == third number')
print('')

while i<max:
    print(numbers[i], numbers[i + 1], numbers[i + 2])
    if numbers[i+1] == numbers[i]**2 and numbers[i+1]**2 == numbers[i+2]:
        print('\tFound: ',numbers[i],numbers[i+1],numbers[i+2])
    i += 1

##############
print('------------------')
print('')
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print('\tFind pairs of strings of the same length')
print('')
i=0
max = len(texts) - 2
while i < max:
    print(texts[i],texts[i+1])

    if len(texts[i]) == len(texts[i+1]):
        print('\tFound: ', texts[i],texts[i+1])
    i += 1
