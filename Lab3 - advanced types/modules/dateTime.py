import datetime

#min and max value
print(datetime.MINYEAR, datetime.MAXYEAR)

#timedelta type
d1 = datetime.timedelta(days=1,hours=2,minutes=30)
print(d1)

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-30)
print(d2)

print("timedelta sum: ",d1+d2)

#date type
print("Today is: ", datetime.date.today())
print("\n")

today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print("Today is: ", today)
print("Bills should be paid within: ",daysToPay.days," days")
print("The bill should be paid till", today + daysToPay)
print("\n")

endOfTheWorld = datetime.date.max
print("The final end of world will happen (by python): ", endOfTheWorld)
print(endOfTheWorld.weekday())
print("\n")

bornDate = datetime.date(1998,11,5)
today = datetime.date.today()
print(today - bornDate)
print("\n")

#datetime type
print("now:\t",datetime.datetime.now())
print("today:\t",datetime.datetime.today())
print("utcnow:\t",datetime.datetime.utcnow())
print("weekday:\t",datetime.datetime.today().weekday())
print("\n")

print("%a", datetime.datetime.now().strftime("%a"))
print("%A", datetime.datetime.now().strftime("%A"))
print("%w", datetime.datetime.now().strftime("%w"))
print("%a %A %w", datetime.datetime.now().strftime("%a %A %w"))
