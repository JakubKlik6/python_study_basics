# If operator
itRains = False

if itRains:
    print("We stay at home")
else:
    print("We go out")
# Ternary operator
print("We stay at home" if itRains else "We go out")

#Zadanie
muscePain = False
fever = True
weakness = True

print("Suspicion of influenza" if muscePain and fever and weakness else "The flu is unlikely")

###########

if muscePain and fever and weakness:
    print("suspicion of influenza")
elif not (muscePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")

###########

isMan = True

if muscePain and fever and weakness:
    print("suspicion of influenza")
elif isMan and (muscePain or fever or weakness):
    print("suspicion of influenza")
else:
    print("Just take a rest")
