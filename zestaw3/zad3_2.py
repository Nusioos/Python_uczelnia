# L = [3, 5, 4] ; L = L.sort()
# blad: Metoda .sort() sortuje listę w miejscu (in-place) i zwraca 'None'.
# Zmienna L po tym przypisaniu przestaje być listą i staje się None.
# Prawidłowo: L = [3, 5, 4]; L.sort() 


# x, y = 1, 2, 3
# blad: ValueError: too many values to unpack (expected 2)
# Skutek: Po lewej stronie mamy 2 zmienne (x, y), a po prawej stronie 3 wartości.
# Prawidłowo: x, y, z = 1, 2, 3


# X = 1, 2, 3 ; X[1] = 4
# blad: TypeError: 'tuple' object does not support item assignment
# Skutek: Zapis z przecinkami bez nawiasów tworzy tuple ktoora jest niemutowalna.
# Prawidłowo X = [1, 2, 3]; X[1] = 4


# X = [1, 2, 3] ; X[3] = 4
# blad: IndexError: list assignment index out of range
# Skutek: Lista ma indeksy 0, 1 i 2. Indeks 3 nie istnieje.
# Prawidłowo (aby dodać element na koniec): X = [1, 2, 3]; X.append(4)


# X = "abc" ; X.append("d")
# blad: AttributeError: 'str' object has no attribute 'append'
# Skutek: Ciągi znaków (stringi) są niemutowalne i nie posiadają metody append().
# Prawidłowo: X = "abc"; X = X + "d" 


# L = list(map(pow, range(8)))
# blad: TypeError: pow() missing required argument 'y' (pos 2)
# Skutek: Funkcja map przekazuje po jednym argumencie z range(8), 
# ale standardowa funkcja pow() wymaga co najmniej dwóch argumentów (podstawy i wykładnika).

