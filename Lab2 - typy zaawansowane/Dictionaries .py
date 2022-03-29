'''             # Dictionaries - consists of a collection of key-value pairs
CountryLeaders = {'PL':'Duda','US':'Trump'}

print(CountryLeaders['US'])  #odwołanie się do elementu

CountryLeaders['DE'] = 'Merkel'    #powiększanie słownika

print(CountryLeaders.keys())       #zostają zwrócone "klucze"
print(CountryLeaders.values())     #zwraca wartości
print(CountryLeaders.items())      #elementy

print(CountryLeaders.setdefault('FR','Macron'))     #wyświetla wartości i dodaje elementy do słownika

NewLeaders = {'RU':'Putin','DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)       #aktualizuje słownik, jeżeli nie znajdzie wartości to ją doda
print(CountryLeaders)
'''

chanels = {'Google':1480,'Email':300,'Natural Traffic':440,'TV Spot':700}
print(chanels['Email'])

chanelsUpdate = {'Natural Traffic':520,'News':600}
chanels.update(chanelsUpdate)
print(chanels.keys())
chanels.pop('Email')
print(chanels)
