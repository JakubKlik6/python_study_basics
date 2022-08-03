'''
1.Zdefiniuj zmienne firstName, famillyName i lastName i przypisz do nich napisy odpowiadające imieniu, nazwisku panieńskim i nowym nazwisku. Następnie utwórz zmienną newName i zapisz w niej wynik konkatenacji (czyli złączenia napisów) dla firstname, spacji, familyName, spacji i lastName. Wyświetl to nowe nazwisko
2. Zdefiniuj zmienną music o następującej zawartości (są to tytuły i autorzy piosenek z filmu Minionki):
"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood 
Uwaga! Ten napis zawiera zarówno apostrof jak i cudzysłów, więc musisz zmodyfikować zapis metodami pokazanymi na tej lekcji, żeby zdefiniowanie zmiennej się udało.
3. W powyższym tekście mowa jest o 3 piosenkach. Zmień tekst tak, aby druga i trzecia piosenka podczas wyswietlania były umieszczone w nowej linii (znowu musisz w tekście dodać pewne znaki specjalne prezentowane na lekcji).
4. Przygotuj kilka poleceń print, które wyświetlą taki oto ascii art:
(\(\ 
( -.-) 
O_(")(")
'''


firstName = 'Kasia'
familyName = 'Sowa'
lastName = 'Mrugala'

newName = firstName+familyName+lastName
print(newName)

newName = firstName+" "+familyName+" "+lastName
print(newName)

music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'

print('(\\(\\') 
print('(-.-)') 
print('O_(")(")')


////////////////////////////////////////////////////////////////////////////////////

'''
1.Utwórz zmienną quote i przypisz jej następującą wartość:   'A good programmer is someone who always looks both ways before crossing a one-way street'
2.Wyświetl tekst napisany tylko wielkimi literami
3.Wyświetl tekst zapisany tylko małymi literami
4.Sprawdź czy tekst kończy się słowem 'street'
5.Sprawdź czy tekst jest zapisany wielkimi literami
6.Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
7.Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo (podnapis)  'one'
8.Zamień w tekście słowo (podnapis) 'one' na '1'
9.Zamień w tekście słowo (podnapis) 'one' na '1' a słowo 'both' na 2
10.Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
11.Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
'''

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print(quote.lower())

quote.endswith('street')

quote.isupper()

quote.upper().isupper()

quote.find('one')

quote.replace('one', '1')

quote.replace('one', '1').replace('both','2')

quote.split(' ')

quote.isdigit()
quote.isdecimal()
quote.isalpha()
quote.isalnum()

////////////////////////////////////////////////////////////////////////////////////

'''
1. Wyświetl napisy: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV. Użyj jednego polecenia print
2. Wyświetl w/w teksty używając jako separatora znaku ";"
3. Korzystając z jednego polecenia print wyświetl napis (bez podtekstów!)
I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV
4. Zadeklaruj zmienne ProgramName o wartości 'BBC', Item o wartości 'News'' i Time o wartości '18:00'.
5. Uwaga: W tym zadaniu nie używaj konkatenacji napisów (łączenia napisów). Użyj tylko polecenia print! Wyświetl napis (zwróć uwagę na kropkę na końcu!)
I like watching News at 18:00 on BBC .
6.  Zmień napis tak, aby kropka była zaraz za  BBC. Nadal nie korzystamy z konkatenacji ale z pojedyńczego polecenia print.
'''

print('TVP1','TVP2','TVN','POLSAT','BBC','HBO','MTV')
print('TVP1','TVP2','TVN','POLSAT','BBC','HBO','MTV',sep =";")
print('I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV')

ProgramName = 'BBC'
Item = 'News'
Time = '18:00'
print('I like watching',Item,'at',Time,'on',ProgramName,'.')

print('I like watching ',Item,' at ',Time,' on ',ProgramName,'.', sep='')
