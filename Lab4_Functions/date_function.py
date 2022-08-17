def GiveWorkingDay():
    import datetime

    day = datetime.date.today()

    if day.weekday() == 5:
        workingday = day + datetime.timedelta(days=2)
    elif day.weekday() == 5:
        workingday = day + datetime.timedelta(days=1)
    else:
        workingday = day

    print("Working day for ",day," is ",workingday)

    return

GiveWorkingDay()

print("------------------------------------\n")

#How many days left to nwe year

def howManyDaysLeft():
    import datetime

    dateToday = datetime.date.today()
    currentYear = dateToday.year
    dateEndYear = datetime.date(currentYear,12,31)
    delta = dateEndYear - dateToday

    print(delta.days)
    return

howManyDaysLeft()

print("------------------------------------\n")
