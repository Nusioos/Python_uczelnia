L = [7, 24, 123, 5, 99]
wynik = "".join(str(liczba).zfill(3) for liczba in L)
print(wynik)