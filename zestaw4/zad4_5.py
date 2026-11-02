def odwracanie_iter(L, left, right):
    """Wersja iteracyjna:"""
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L, left, right):
    """Wersja rekurencyjna:"""
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)

odwracanie = odwracanie_iter


if __name__ == "__main__":
    for f in (odwracanie_iter, odwracanie_rek):
        L = [0, 1, 2, 3, 4, 5, 6]
        f(L, 2, 5)
        print(f.__name__, L)   # [0, 1, 5, 4, 3, 2, 6]

        L = [1, 2, 3]
        f(L, 1, 1)             
        print(L)               