def suma_dlugosci_wyrazow(tekst):
     slowo = tekst.split()
     najd=max(slowo,key=len)
     dlugosc=len(najd)

     print(najd, "slowo")
     print(dlugosc, "dlugosc slowa")

line = "Zajecia python odbywaja sie w srody o godzinie 12:00 programuje sie tam czy cos 2"
suma_dlugosci_wyrazow(line)
