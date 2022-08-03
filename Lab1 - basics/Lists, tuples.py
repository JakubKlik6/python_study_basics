"""
Tax = (1, 2, 3, 4)     #tuple - ___(), is a collection which is ordered and unchangeable.

print(Tax)
print(Tax[1])
print(Tax.index(1))
print(Tax.count(1))
print(max(Tax))

Taxlist = list(Tax)
print(Taxlist)          #zamiana tuple na list

(tax1, tax2, tax3 ,tax4) = Tax
print(tax1,tax2,tax3,tax4)      #assigment 4 variables

a = 5
b = 10
(a,b) = (b,a)
print("a =",a,"b =",b)
"""

Marketing = ["loyality program", "client promotion" ,"market research"]
Marketing.append("public relations")
print(Marketing[3])
Marketing.insert(3,"investor relations")

emailMarketing = list(Marketing)        #kopiowanie elementów listy marketing do listy emailMarketing
print(emailMarketing)
emailMarketing.sort()

internalEmails = ["internal communication"]
emailMarketing.extend(internalEmails)           #dodawanie list

emailTuple = tuple(emailMarketing)
print(emailTuple)




