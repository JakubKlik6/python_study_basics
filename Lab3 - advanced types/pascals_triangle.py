width = 60
heigh = 8

numbers = [1]

line = ''
for n in numbers:
    line += "%3d" % (n)
print(line.center(width))


for i in range(heigh):
    newNumber = [1]
    position = 0
    while position < len(numbers) - 1:
        newNumber.append(numbers[position] + numbers[position+1])
        position += 1

    newNumber.append(1)

    numbers = newNumber.copy()

    line = ''
    for n in numbers:
        line += "%3d" % (n)
    print(line.center(width))

