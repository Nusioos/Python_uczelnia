def roman2int(tekst_rzymski: str) -> int:

    slownik = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    wynik = 0
    n = len(tekst_rzymski)
    
    for i in range(n):
        aktualna_wartosc = slownik[tekst_rzymski[i]]
        
        if i + 1 < n and aktualna_wartosc < slownik[tekst_rzymski[i + 1]]:
            wynik -= aktualna_wartosc
        else:
            wynik += aktualna_wartosc
            
    return wynik

print(roman2int("IX"))    # 9
print(roman2int("XIV"))   # 14
print(roman2int("MMXXIV")) # 2024