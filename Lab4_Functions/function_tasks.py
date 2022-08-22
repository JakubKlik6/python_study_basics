import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having 

    value = a1*pow(factor,index-1)
    return value

print('element 64 =',GiveGeomSeqElement(1,2,64))


print('------------------------------------------------')


a1=3
factor=2
maxindex=10
#for lopp that will print all parameters
for i in range(1,maxindex):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)


print('------------------------------------------------')


def GiveFactorForGeomSeq(term ,nextterm ):
    return nextterm / term

print(GiveFactorForGeomSeq(12,24))


print('------------------------------------------------')


def GiveSumOfNElementsGeomSeq(a1 = 2,factor = 2,n = 2):
    sum = a1 * (1 - pow(factor,n)) / (1 - factor)
    return sum

print("Sum = ",GiveSumOfNElementsGeomSeq(2,3,4))


print('------------------------------------------------')
