def analiza_sekwencji(sek1, sek2):
    zbior1 = set(sek1)
    zbior2 = set(sek2)
    
    wspolne = list(zbior1.intersection(zbior2))
    wszystkie = list(zbior1.union(zbior2))
    
    return wspolne, wszystkie


sekwencja_1 = [1, 2, 3, 4, 2, 1]
sekwencja_2 = [3, 4, 5, 6, 4]

wynik_a, wynik_b = analiza_sekwencji(sekwencja_1, sekwencja_2)

print("(a) Lista elementów wspólnych:", wynik_a)
print("(b) Lista wszystkich elementów:", wynik_b)