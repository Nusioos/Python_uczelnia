def oblicz_sumy_sekwencji(lista_sekwencji):
    return [sum(sekwencja) for sekwencja in lista_sekwencji]

wejscie = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
wynik = oblicz_sumy_sekwencji(wejscie)

print("Wynik:", wynik)
