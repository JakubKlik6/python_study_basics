
countries = ['US','FR',3,15]        #tworzenie listy

countries[2] = 'GB'                 #przypisywanie wartości na dane miejsce (zastępowanie)

print(countries[1])                 #wypisywanie danej wartości z listy

countries.append('PL')              #dodawanie elementu do listy

countries.insert(2,'ES')            #dodawanie elementu do listy na dane miejsce

countries.remove('PL')              #usuwanie elementu

countries.sort()                    #sortowanie listy

countries.reverse()                 #odwracanie listy

print(countries.pop(2))             #zwaraca, a następnie usuwa element

print(countries.index('ES'))        #sprawdzenie pozycji elementu

print(countries.count('PL'))        #sprawdzamy ile razy dana wartość występuje w liście

newList = ['FI','SE']
countries.extend(newList)           #dodawanie listy do listy

countriesCopy = countries           #kopiowanie listy (dodatkowa nazwa, miejsce w pamięci jest to samo)
countriesCopy.clear()               #czyści elementy listy i zostawia pustą listę

countries.copy = newcountries       #kopiowanie listy

print(countries)


hitsTitles = ['Brothers in arms','Bohemian Rhapsody','Stairway to heaven','Riders on the storm','Wish you were here']
helpTitle = ['Child in time','Again']
hitsTitles.extend(helpTitle)
hitsTitles.insert(3,'Hotel California')
hitsTitles.insert(1,'The sound of silence')
print(hitsTitles.index('Hotel California'))
hitsTitles.remove('Hotel California')
hitsTitles.insert(1, 'Enjoy the silence')
hitsTitlescopy = hitsTitles
hitsTitlescopy.reverse()
hitsTitlescopy.sort()
print(hitsTitlescopy.pop(0))
print(hitsTitlecopy.pop(1))
additionalSongs  = ['Nothing comapres 2 u','Wish you were here']
hitsTitles.extend(additionalSongs)
print(hitsTitles.index('WISH YOU WERE HERE'))
print(hitsTitles.index('RIDERS ON THE STORM'))
hitsTitlescopy.clear()

