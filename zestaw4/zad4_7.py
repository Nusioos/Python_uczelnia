def flatten(sequence):
    """Zwraca spłaszczoną listę wszystkich elementów (dowolna głębokość zagnieżdżenia)."""
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))   
        else:
            result.append(item)
    return result



if __name__ == "__main__":
    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print(flatten(sequence))          # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(flatten([]))                # []
    print(flatten([[], [[]], ()]))    # []
    print(flatten([1, [2, [3, [4]]]]))  # [1, 2, 3, 4]