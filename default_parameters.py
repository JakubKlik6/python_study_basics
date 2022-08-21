import datetime

def GiveWorkingDay(year, month=datetime.date.today().month, day=datetime.date.today().day):

    day = datetime.date(year,month,day)

    if day.weekday() == 5:
        workingday = day + datetime.timedelta(days=2)
    elif day.weekday() == 5:
        workingday = day + datetime.timedelta(days=1)
    else:
        workingday = day

    print("Working day for ",day," is ",workingday)

    return

GiveWorkingDay(2016)
GiveWorkingDay(1995)
