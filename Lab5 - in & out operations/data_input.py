def check_int(x):
    if x[0] in ('-','+'):
        return x[1:].isdigit()
    return x.isdigit()

print('This program solves equation ax^2+bx+c = 0')

print("Enter a: ")
a_str = input()
print("Enter b: ")
b_str = input()
print("Enter c: ")
c_str = input()


if not check_int(a_str) and check_int(b_str) and check_int(c_str):
    print("Error! You enter wrong value, please enter digit integer")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a == 0:
        print(" a = 0!!! - > This is not quadratic equation, please enter correct values")
    else:
        delta = b**2 - 4 * a * c

        if delta < 0:
            print("There are no solutions")
        elif delta == 0:
            x0 = - b / 2 * a
            print("There is one solution x1 = %.2f" % x0)
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print("There are two solutions x1 = %.2f and x2 = %.2f" % (x1, x2) )
