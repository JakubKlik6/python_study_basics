import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print("Quantity of tab inputdata: ",len(inputdata))
print("Quantity of tab factortable: ",len(factortable))
print("\n")

if len(inputdata) == len(factortable):
    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print("minvalue = ",minvalue,"maxvalue = ", maxvalue)

        miniteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(miniteger,"\t",inputdata[i],"\t",maxinteger)
        i+=1
else:
    print("Inputdata and factortable need to have equal number of elements")

print('--------------------------------------------------------------------',"\n")

import random

for i in range(10):
    inputdata = random.uniform(0,1)
    factortable = random.uniform(0,1)
    i = 0
    while i < inputdata:
        minvalue = inputdata - factortable * inputdata
        maxvalue = inputdata + factortable * inputdata
        print("minvalue = ", round(minvalue,2), "maxvalue = ", round(maxvalue,2))

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata, "\t", maxinteger)
        i += 1
else:
    print("Inputdata and factortable need to have equal number of elements")


print('--------------------------------------------------------------------',"\n")

import datetime

print(datetime.datetime.now())
print('results generated:',datetime.date.today().strftime("%Y-%m-%d"))
