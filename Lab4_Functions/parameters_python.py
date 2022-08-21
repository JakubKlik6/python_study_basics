def PrintAnimal():
    print("What animal you want to see?")
    print("\n")
    animal = input()

    # this function prints a cat ascii-art
    if animal == "cat":
        txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
        print(txt)

    # this function prints a bear ascii-art
    elif animal == "bear":
        txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
        print(txt)

    # this function prints a bat ascii-art
    elif animal == "bat":
        txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
        print(txt)
    else:
        print("U can only choose cat, bat or bear")

    return


PrintAnimal()

print("__________________________________")


def DaysToEndOfYear(year,month,day):
    from datetime import date

    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)

DaysToEndOfYear(1915,4,20)
