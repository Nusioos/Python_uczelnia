def suma_dlugosci_wyrazow(tekst):
    return sum(len(slowo) for slowo in tekst.split())
line = "Zajecia python odbywaja sie w srody o godzinie 12:00 \n programuje sie tam czy cos 2"
wynik = suma_dlugosci_wyrazow(line)

print("len:", wynik)