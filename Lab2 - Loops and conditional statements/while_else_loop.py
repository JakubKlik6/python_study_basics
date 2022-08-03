#while/else loop
row = 1
last_row = 31
while row <= last_row :
    print('Row number',row)
    row += 1
else:
    print('out of space')

################

xmas = 1
max_xmas = 10
while xmas <= max_xmas:
    print(xmas*' x')
    xmas += 1

################

number = 1
max_number = 13
while number <= max_number:
    print('Liczba', number)
    print('kwadrat: ', number * number,'Sześcian: ', number * number * number)
    number += 1

################

poweroftwo = 0
limit = 16
while poweroftwo <= limit:
    print('2 ^',poweroftwo,' = ',2**poweroftwo)
    poweroftwo += 1
