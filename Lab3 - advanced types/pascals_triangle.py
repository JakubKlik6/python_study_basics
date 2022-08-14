numbers = [1]       #creating numbers list

for i in range(5):      #range of triangle
    newNumber = [1]
    position = 0
    while position < len(numbers) - 1:
        newNumber.append(numbers[position] + numbers[position+1])       #sum of two numbers if condition is met
        position += 1       #next position

    newNumber.append(1)     #adding 1 on the edges

    numbers = newNumber.copy()      #rewrite the values

    print(numbers)
