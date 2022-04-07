#zagnieżdżony if, mniej przejrzysty
age = 27
isDrunk = False
isRestrictedArea = False

if age < 18:
    print("U cant buy alcohol here")
else:
    if isDrunk:
        print("Are u Drunk?!")
    else:
        if isRestrictedArea:
            print("Restricted area")
        else:
            print("Ok, here u go")

print("______________________")

#notacja 2, bardziej przejrzysta

if age < 18:
    print("U cant buy alcohol here, you're too young")
elif isDrunk:
    print("Are u Drunk?!")
elif isRestrictedArea:
    print("Restricted area")
else:
    print("Ok, here u go")

