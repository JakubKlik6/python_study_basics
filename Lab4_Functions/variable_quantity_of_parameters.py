def PrintAnimal(*animals):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
    |\---/|
    | o_o |
     \_^_/'''
    txt_bear = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    txt_bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
    for animal in animals:
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)

    return

PrintAnimal('cat','bat')


print("--------------------")


import datetime

def DaysToEndOfYear(*dates):
    for date in dates:

        date_end_year = datetime.date(date.year,12,31)
        delta = date_end_year - date
        print('Date',date,'days to end of the year',delta.days)

DaysToEndOfYear(datetime.date(1999,1,15))
print('----------------')
DaysToEndOfYear(datetime.date(1999,1,15),datetime.date(2009,1,15))
print('----------------')
DaysToEndOfYear(datetime.date(1999,1,15),datetime.date(2009,1,15),datetime.date(2019,1,15))
print('----------------')
