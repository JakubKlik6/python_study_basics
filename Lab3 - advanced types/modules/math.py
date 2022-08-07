#math module
import math

degree = 360

degree_rad = (degree * math.pi) / 180
print("%d degree is %f radians" % (degree, degree_rad))
print(math.radians(degree))

print("\n")

degree = 45
degree_rad = (degree * math.pi) / 180
print("%d degree is %f radians" % (degree, degree_rad))
print(math.radians(degree))

print("\n")

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r **2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2

print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)
print('')
print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)
print('')

math_ls = dir(math)
print(math_ls)
