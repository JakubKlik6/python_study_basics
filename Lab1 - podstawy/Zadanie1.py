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






